# vllm-project/vllm#32436: [Bug]: GLM 4.7 Tool Call issue

| 字段 | 值 |
| --- | --- |
| Issue | [#32436](https://github.com/vllm-project/vllm/issues/32436) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM 4.7 Tool Call issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 工具调用有问题tool-call-parser glm47 容易出现问题，使用Claude Code非最新版本容易报错，用langchain开发的智能体也会报错！ 见modelscope https://www.modelscope.cn/models/ZhipuAI/GLM-4.7/feedback (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] Failed to extract tool call spec (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] Traceback (most recent call last): (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] File "/usr/local/lib/python3.12/dist-packages/vllm/tool_parsers/glm4_moe_tool_parser.py", line 104, in extract_tool_calls (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] pairs = self.func_arg_regex.findall(tc_args) (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] TypeError: expected string or buffer 应该是vllm glm47工具解析器的bug https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/glm47_moe_tool_parser.py 这个新的解析器直接继承了旧的 https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/glm4_moe_tool_parser.py 好像正则表达式写得不好，空参数的工具调用就直接挂了 ### Before submitting a new i...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 容易报错，用langchain开发的智能体也会报错！ 见modelscope https://www.modelscope.cn/models/ZhipuAI/GLM-4.7/feedback (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] Failed to extract tool call spec (APIServer pid=1) ER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -call-parser glm47 容易出现问题，使用Claude Code非最新版本容易报错，用langchain开发的智能体也会报错！ 见modelscope https://www.modelscope.cn/models/ZhipuAI/GLM-4.7/feedback (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] Failed to...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: s/ZhipuAI/GLM-4.7/feedback (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] Failed to extract tool call spec (APIServer pid=1) ERROR 12-24 17:16:37 [glm4_moe_tool_parser.py:123] Traceback (most recen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
