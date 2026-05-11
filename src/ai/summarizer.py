"""Daily summary generation — pure programmatic rendering."""

import re
from typing import List, Dict, Any

from ..market.constants import DEFAULT_FALSIFIER
from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Diplomacy & Markets Brief",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 外交与金融观察",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> From {total_fetched} items, {len(items)} important content pieces were selected\n\n"
            "---\n\n"
        )

        # TOC
        toc_entries = []
        for i, item in enumerate(items):
            _t = item.metadata.get(f"title_{language}") or item.title
            t = str(_t).replace("[", "(").replace("]", ")")
            if language == "zh":
                t = _pangu(t)
            score = item.ai_score or "?"
            toc_entries.append(f"{i + 1}. [{t}](#item-{i + 1}) \u2b50\ufe0f {score}/10")
        toc = "\n".join(toc_entries) + "\n\n---\n\n"

        parts = [self._format_item(item, labels, language, i + 1) for i, item in enumerate(items)]

        return header + toc + "".join(parts)

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        entries = []
        for i, item in enumerate(items, start=1):
            title = str(item.metadata.get(f"title_{language}") or item.title).replace("[", "(").replace("]", ")")
            if language == "zh":
                title = _pangu(title)
            score = item.ai_score or "?"
            entries.append(f"{i}. [{title}]({item.url}) \u2b50\ufe0f {score}/10")

        return header + "\n".join(entries)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            day = item.published_at.strftime("%d").lstrip("0")
            source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        lines = [
            f'<a id="item-{index}"></a>',
            f"## [{title}]({url}) \u2b50\ufe0f {score}/10",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        trading_analysis = meta.get("trading_analysis")
        is_asset_watchlist = (
            isinstance(trading_analysis, dict)
            and trading_analysis.get("question_type") == "asset_watchlist"
        )

        if not is_asset_watchlist:
            forecast_block = self._format_forecast_block(meta.get("forecast"))
            if forecast_block:
                lines.append("")
                lines.append(forecast_block)

        trading_block = self._format_trading_analysis_block(
            trading_analysis,
            meta.get("forecast"),
        )
        if trading_block:
            lines.append("")
            lines.append(trading_block)

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    @staticmethod
    def _as_list(value: Any) -> List[str]:
        """Convert unknown values into a cleaned string list."""
        if isinstance(value, list):
            cleaned = []
            for item in value:
                if isinstance(item, (str, int, float, bool)):
                    text = str(item).strip()
                    if text:
                        cleaned.append(text)
            return cleaned
        if isinstance(value, str) and value.strip():
            return [value.strip()]
        return []

    @staticmethod
    def _join_items(value: Any, default: str = "暂无") -> str:
        """Join list-like values into a human-readable line."""
        items = DailySummarizer._as_list(value)
        return "；".join(items) if items else default

    @staticmethod
    def _to_percent(value: Any) -> str:
        """Render probability values as percent text."""
        if isinstance(value, (int, float)):
            return f"{value:.0f}%"
        if isinstance(value, str) and value.strip():
            return value.strip()
        return "-"

    @staticmethod
    def _clean_table_cell(value: Any) -> str:
        """Clean text for safe Markdown table cells by flattening newlines and pipes."""
        text = str(value or "").replace("\n", " ").replace("|", "/").strip()
        return text

    @staticmethod
    def _to_probability_number(value: Any) -> str:
        """Render probability values as compact whole numbers for overview cells."""
        if isinstance(value, (int, float)):
            return f"{value:.0f}"
        text = DailySummarizer._clean_table_cell(value).rstrip("%")
        if not text:
            return "-"
        try:
            return f"{float(text):.0f}"
        except ValueError:
            return text

    def _format_forecast_block(self, forecast: Any) -> str:
        """Render the forecast analysis block in Chinese if available."""
        if not isinstance(forecast, dict):
            return ""

        is_forecastable = forecast.get("is_forecastable")
        if is_forecastable is False:
            reason = str(forecast.get("reason") or "未提供")
            return f"**预测分析**：该事件不适合进行独立情景预测。原因：{reason}"
        if not is_forecastable:
            return ""

        cause_chain = forecast.get("cause_chain") if isinstance(forecast.get("cause_chain"), dict) else {}
        scenarios_raw = forecast.get("scenarios") if isinstance(forecast.get("scenarios"), list) else []
        scenarios_by_name = {
            str(s.get("name", "")).strip().lower(): s
            for s in scenarios_raw
            if isinstance(s, dict)
        }
        near_term_watch = (
            forecast.get("near_term_watch")
            if isinstance(forecast.get("near_term_watch"), dict)
            else {}
        )
        confidence = forecast.get("confidence") if isinstance(forecast.get("confidence"), dict) else {}

        actor_lines = []
        if isinstance(forecast.get("actors"), list):
            for actor in forecast.get("actors"):
                if not isinstance(actor, dict):
                    actor_text = str(actor).strip()
                    if actor_text:
                        actor_lines.append(f"- {actor_text}")
                    continue
                name = str(actor.get("name") or "未知行为体")
                incentives = self._join_items(actor.get("likely_incentives"))
                role = str(actor.get("role") or "").strip()
                role_text = f"（{role}）" if role else ""
                actor_lines.append(f"- {name}{role_text}：{incentives}")
        if not actor_lines:
            actor_lines.append("- 暂无")

        scenario_specs = [
            ("baseline", "基准"),
            ("escalation", "升级"),
            ("deescalation", "缓和"),
            ("wildcard", "意外"),
        ]
        scenario_rows = []
        for key, label in scenario_specs:
            scenario = scenarios_by_name.get(key, {})
            horizon = self._clean_table_cell(scenario.get("horizon") or "-")
            probability = self._clean_table_cell(self._to_percent(scenario.get("probability")))
            reasoning = self._clean_table_cell(scenario.get("reasoning") or "-")
            triggers = self._clean_table_cell(
                self._join_items(scenario.get("trigger_conditions"), default="-")
            )
            scenario_rows.append(f"| {label} | {horizon} | {probability} | {reasoning} | {triggers} |")

        confidence_level_map = {
            "low": "低",
            "medium": "中等",
            "high": "高",
        }
        confidence_level = str(confidence.get("level") or "medium").lower()
        confidence_label = confidence_level_map.get(confidence_level, "中等")
        confidence_reason = str(confidence.get("reason") or "")
        confidence_text = f"{confidence_label}。{confidence_reason}" if confidence_reason else confidence_label

        lines = [
            "**预测分析**",
            "",
            f"**事件类型**：{forecast.get('event_type') or '未说明'}",
            "",
            "**原因链**",
            f"- 直接触发：{cause_chain.get('immediate_trigger') or '暂无'}",
            f"- 深层原因：{self._join_items(cause_chain.get('structural_causes'))}",
            f"- 约束条件：{self._join_items(cause_chain.get('constraints'))}",
            "",
            "**主要行为体与激励**",
            *actor_lines,
            "",
            "**未来情景**",
            "| 情景 | 时间窗口 | 概率 | 逻辑 | 触发条件 |",
            "|---|---:|---:|---|---|",
            *scenario_rows,
            "",
            "**观察指标**",
            f"- 24小时：{self._join_items(near_term_watch.get('24h'))}",
            f"- 7天：{self._join_items(near_term_watch.get('7d'))}",
            f"- 30天：{self._join_items(near_term_watch.get('30d'))}",
            "",
            f"**置信度**：{confidence_text}",
            "",
            "**反证条件**",
        ]

        falsifiers = self._as_list(forecast.get("falsifiers")) or ["暂无"]
        lines.extend([f"- {item}" for item in falsifiers])

        lines += [
            "",
            "**信息缺口**",
        ]
        missing_evidence = self._as_list(forecast.get("missing_evidence")) or ["暂无"]
        lines.extend([f"- {item}" for item in missing_evidence])

        lines += [
            "",
            "**市场或政策影响**",
        ]
        implications = self._as_list(forecast.get("market_or_policy_implications")) or ["暂无"]
        lines.extend([f"- {item}" for item in implications])

        return "\n".join(lines)

    def _format_trading_analysis_block(self, trading_analysis: Any, forecast: Any = None) -> str:
        """Render market trading analysis details when available."""
        if not isinstance(trading_analysis, dict):
            return ""

        question_type = str(trading_analysis.get("question_type") or "generic_market_event")

        if question_type == "asset_watchlist":
            return self._format_asset_watchlist_block(trading_analysis)

        market_question = str(trading_analysis.get("market_question") or "N/A")
        signals = trading_analysis.get("signals") if isinstance(trading_analysis.get("signals"), list) else []
        resonance = self._as_list(trading_analysis.get("resonance")) or ["N/A"]
        divergences = self._as_list(trading_analysis.get("divergences")) or ["N/A"]
        scenarios = trading_analysis.get("scenarios") if isinstance(trading_analysis.get("scenarios"), list) else []
        monitor_signals = (
            trading_analysis.get("monitor_signals")
            if isinstance(trading_analysis.get("monitor_signals"), list)
            else []
        )
        errors = self._as_list(trading_analysis.get("errors"))
        forecast_falsifiers = self._as_list(forecast.get("falsifiers")) if isinstance(forecast, dict) else []
        data_sources = self._as_list(trading_analysis.get("data_sources")) or ["N/A"]

        signal_rows = []
        for signal in signals:
            if not isinstance(signal, dict):
                continue
            signal_rows.append(
                "| {layer} | {signal} | {value} | {interpretation} |".format(
                    layer=self._clean_table_cell(signal.get("layer", "-")),
                    signal=self._clean_table_cell(signal.get("signal", "-")),
                    value=self._clean_table_cell(signal.get("value", "-")),
                    interpretation=self._clean_table_cell(signal.get("interpretation", "-")),
                )
            )
        if not signal_rows:
            signal_rows.append("| - | - | - | - |")

        scenario_rows = []
        for scenario in scenarios:
            if not isinstance(scenario, dict):
                continue
            probability = self._clean_table_cell(scenario.get("probability", "-"))
            if probability not in {"", "-"} and not probability.endswith("%"):
                probability = f"{probability}%"
            scenario_rows.append(
                "| {name} | {probability} | {bias} |".format(
                    name=self._clean_table_cell(scenario.get("name", "-")),
                    probability=probability or "-",
                    bias=self._clean_table_cell(scenario.get("trading_bias", "-")),
                )
            )
        if not scenario_rows:
            scenario_rows.append("| - | - | - |")

        monitor_rows = []
        for monitor in monitor_signals:
            if not isinstance(monitor, dict):
                continue
            monitor_rows.append(
                "| {signal} | {threshold} | {meaning} |".format(
                    signal=self._clean_table_cell(monitor.get("signal", "-")),
                    threshold=self._clean_table_cell(monitor.get("threshold", "-")),
                    meaning=self._clean_table_cell(monitor.get("meaning", "-")),
                )
            )
        if not monitor_rows:
            monitor_rows.append("| - | - | - |")

        lines = [
            "**Trading Analysis**",
            "",
            f"- 分析类型 (Event Type): {question_type}",
            "",
            "### 市场问题 (Market Question)",
            market_question,
            "",
            "### 数据摘要 (Data Summary)",
            "| Layer | Signal | Current Reading | Trading Meaning |",
            "|---|---|---:|---|",
            *signal_rows,
            "",
            "### 共振信号 (Resonance Signals)",
            *[f"- {entry}" for entry in resonance],
            "",
            "### 关键分歧 (Key Divergences)",
            *[f"- {entry}" for entry in divergences],
            "",
            "### 概率估计 (Probability Estimates)",
            "| 情景 | 概率 | 方向偏好 |",
            "|---|---:|---|",
            *scenario_rows,
            "",
            "### 观察指标 (Signals to Monitor)",
            "| Signal | Threshold | Meaning |",
            "|---|---:|---|",
            *monitor_rows,
            "",
            "### 反证条件 (Falsifiers)",
            *[f"- {entry}" for entry in (forecast_falsifiers or [DEFAULT_FALSIFIER])],
            "",
            "### 数据来源 (Data Sources)",
            *[f"- {entry}" for entry in data_sources],
        ]
        if errors:
            lines.extend(["", "### 信息缺口 (Missing Evidence)", *[f"- {entry}" for entry in errors]])
        return "\n".join(lines)

    def _format_asset_watchlist_block(self, trading_analysis: dict) -> str:
        """Render asset_watchlist mode trading analysis block."""
        asset_views = (
            trading_analysis.get("asset_views")
            if isinstance(trading_analysis.get("asset_views"), list)
            else []
        )
        errors = self._as_list(trading_analysis.get("errors"))
        data_sources = self._as_list(trading_analysis.get("data_sources")) or ["N/A"]

        lines = [
            "**Trading Analysis**",
            "",
            "> 分析类型：固定资产池概率分析 (Asset Watchlist)  ",
            "> 分析范围：QDII 纳斯达克 100 / 海外股票 / 美国股票 / 日本股票 / 香港股票  ",
            "> 时间维度：1日 / 1周 / 1月  ",
            "> 免责声明：本分析仅基于市场数据进行概率估算，不构成投资建议。",
            "",
        ]

        if asset_views:
            # Overview table
            lines += [
                "### 资产概率总览 (Asset Probability Overview)",
                "",
                "| 资产 | 市场 | 1日 | 1周 | 1月 | 数据质量 |",
                "|---|---|---|---|---|---|",
            ]
            for av in asset_views:
                if not isinstance(av, dict):
                    continue
                horizons = av.get("horizons") or []
                cells = {"1d": {}, "1w": {}, "1m": {}}
                for hp in horizons:
                    if isinstance(hp, dict):
                        hz = hp.get("horizon", "")
                        if hz in cells:
                            cells[hz] = hp
                def _fmt_cell(hp: dict) -> str:
                    if not hp:
                        return "-"
                    bias = self._clean_table_cell(hp.get("expected_bias", "-"))
                    up = self._to_probability_number(hp.get("up_probability", 0))
                    dn = self._to_probability_number(hp.get("down_probability", 0))
                    ne = self._to_probability_number(hp.get("neutral_probability", 0))
                    return self._clean_table_cell(f"{bias} {up}/{dn}/{ne}")
                v1d = _fmt_cell(cells["1d"])
                v1w = _fmt_cell(cells["1w"])
                v1m = _fmt_cell(cells["1m"])
                dq = self._clean_table_cell(av.get("data_quality", "medium"))
                lines.append(
                    f"| {self._clean_table_cell(av.get('name', '-'))} | {self._clean_table_cell(av.get('market', '-'))} "
                    f"| {v1d} | {v1w} | {v1m} | {dq} |"
                )

            # Detailed per-asset views
            lines += ["", "### 详细资产分析 (Detailed Asset Views)"]
            for av in asset_views:
                if not isinstance(av, dict):
                    continue
                proxy_note = " *(代理品种)*" if av.get("analysis_proxy") else ""
                lines += [
                    "",
                    f"#### {av.get('name', 'Unknown')}{proxy_note}",
                    "",
                ]
                if av.get("note"):
                    lines += [f"> {av['note']}", ""]
                syms = ", ".join(av.get("symbols") or [])
                lines += [
                    f"市场：{av.get('market', '-')}",
                    f"品种：{syms or '-'}",
                    "",
                    "| 周期 | 上涨概率 | 下跌概率 | 中性概率 | 偏向 | 置信度 |",
                    "|---|---:|---:|---:|---|---|",
                ]
                for hp in (av.get("horizons") or []):
                    if not isinstance(hp, dict):
                        continue
                    hz_label = {"1d": "1日", "1w": "1周", "1m": "1月"}.get(hp.get("horizon", ""), hp.get("horizon", "-"))
                    lines.append(
                        f"| {self._clean_table_cell(hz_label)} | {self._clean_table_cell(self._to_percent(hp.get('up_probability', 0)))} "
                        f"| {self._clean_table_cell(self._to_percent(hp.get('down_probability', 0)))} "
                        f"| {self._clean_table_cell(self._to_percent(hp.get('neutral_probability', 0)))} "
                        f"| {self._clean_table_cell(hp.get('expected_bias', '-'))} "
                        f"| {self._clean_table_cell(hp.get('confidence', '-'))} |"
                    )
                lines += [""]
                if any(hp.get("basis") for hp in (av.get("horizons") or []) if isinstance(hp, dict)):
                    lines.append("**分析依据 (Basis)**")
                    for hp in (av.get("horizons") or []):
                        if not isinstance(hp, dict) or not hp.get("basis"):
                            continue
                        hz_label = {"1d": "1日", "1w": "1周", "1m": "1月"}.get(hp.get("horizon", ""), hp.get("horizon", "-"))
                        lines.append(f"- {hz_label}: {hp['basis']}")
                    lines.append("")
                if any(hp.get("invalidation") for hp in (av.get("horizons") or []) if isinstance(hp, dict)):
                    lines.append("**反证条件 (Invalidation)**")
                    for hp in (av.get("horizons") or []):
                        if not isinstance(hp, dict) or not hp.get("invalidation"):
                            continue
                        hz_label = {"1d": "1日", "1w": "1周", "1m": "1月"}.get(hp.get("horizon", ""), hp.get("horizon", "-"))
                        lines.append(f"- {hz_label}: {hp['invalidation']}")
                    lines.append("")
                if av.get("conclusion"):
                    lines += [f"**结论**：{av['conclusion']}", ""]

        if errors:
            lines += ["### 信息缺口 (Missing Evidence)", *[f"- {entry}" for entry in errors], ""]
        lines += [
            "### 数据来源 (Data Sources)",
            *[f"- {entry}" for entry in data_sources],
            "",
            "> *以上分析仅为市场数据概率模型输出，不构成投资建议。*",
        ]
        return "\n".join(lines)

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> Analyzed {total_fetched} items, but none met the importance threshold.\n\n"
            + labels["empty_body"]
        )
