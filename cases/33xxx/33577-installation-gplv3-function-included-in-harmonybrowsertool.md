# vllm-project/vllm#33577: [Installation]: GPLv3 function included in HarmonyBrowserTool

| 字段 | 值 |
| --- | --- |
| Issue | [#33577](https://github.com/vllm-project/vllm/issues/33577) |
| 状态 | open |
| 标签 | installation;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: GPLv3 function included in HarmonyBrowserTool

### Issue 正文摘录

The HarmonyBrowserTool [imports ExaBackend](https://github.com/vllm-project/vllm/blob/ffe1fc7a28841973135b981fb68ce515b409a236/vllm/entrypoints/mcp/tool.py#L71) from gpt_oss.tools.simple_browser. ExaBackend makes various [calls](https://github.com/openai/gpt-oss/blob/599476783c6f88508dab8577808b5ead5cbee8d2/gpt_oss/tools/simple_browser/backend.py#L163) to [process_html](https://github.com/openai/gpt-oss/blob/599476783c6f88508dab8577808b5ead5cbee8d2/gpt_oss/tools/simple_browser/page_contents.py#L253), which subsequently calls [html_to_text](https://github.com/openai/gpt-oss/blob/599476783c6f88508dab8577808b5ead5cbee8d2/gpt_oss/tools/simple_browser/page_contents.py#L185). This function makes use of [html2text](https://github.com/openai/gpt-oss/blob/599476783c6f88508dab8577808b5ead5cbee8d2/gpt_oss/tools/simple_browser/page_contents.py#L192C22-L192C31), which is covered under [GPLv3](https://github.com/Alir3z4/html2text?tab=GPL-3.0-1-ov-file). As a result of this call chain, would certain vLLM configurations be subject to GPLv3 instead of the current Apache license?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: GPLv3 function included in HarmonyBrowserTool installation;stale The HarmonyBrowserTool [imports ExaBackend](https://github.com/vllm-project/vllm/blob/ffe1fc7a28841973135b981fb68ce515b409a236/vllm/entryp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mple_browser. ExaBackend makes various [calls](https://github.com/openai/gpt-oss/blob/599476783c6f88508dab8577808b5ead5cbee8d2/gpt_oss/tools/simple_browser/backend.py#L163) to [process_html](https://github.com/openai/gp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: HarmonyBrowserTool installation;stale The HarmonyBrowserTool [imports ExaBackend](https://github.com/vllm-project/vllm/blob/ffe1fc7a28841973135b981fb68ce515b409a236/vllm/entrypoints/mcp/tool.py#L71) from gpt_oss.tools.s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nstallation]: GPLv3 function included in HarmonyBrowserTool installation;stale The HarmonyBrowserTool [imports ExaBackend](https://github.com/vllm-project/vllm/blob/ffe1fc7a28841973135b981fb68ce515b409a236/vllm/entrypoi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
