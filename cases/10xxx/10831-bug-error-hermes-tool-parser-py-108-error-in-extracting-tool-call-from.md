# vllm-project/vllm#10831: [Bug]: ERROR hermes_tool_parser.py:108] Error in extracting tool call from response.

| 字段 | 值 |
| --- | --- |
| Issue | [#10831](https://github.com/vllm-project/vllm/issues/10831) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ERROR hermes_tool_parser.py:108] Error in extracting tool call from response.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This error occurred when I used the Qwen2.5-72B-AWQ model to make tool calls (with `stream=False`) ``` ERROR 12-02 05:59:06 hermes_tool_parser.py:108] Error in extracting tool call from response. ERROR 12-02 05:59:06 hermes_tool_parser.py:108] Traceback (most recent call last): ERROR 12-02 05:59:06 hermes_tool_parser.py:108] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py", line 87, in extract_tool_calls ERROR 12-02 05:59:06 hermes_tool_parser.py:108] json.loads(match[0] if match[0] else match[1]) ERROR 12-02 05:59:06 hermes_tool_parser.py:108] File "/usr/lib/python3.12/json/__init__.py", line 346, in loads ERROR 12-02 05:59:06 hermes_tool_parser.py:108] return _default_decoder.decode(s) ERROR 12-02 05:59:06 hermes_tool_parser.py:108] ^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 12-02 05:59:06 hermes_tool_parser.py:108] File "/usr/lib/python3.12/json/decoder.py", line 337, in decode ERROR 12-02 05:59:06 hermes_tool_parser.py:108] obj, end = self.raw_decode(s, idx=_w(s, 0).end()) ERROR 12-02 05:59:06 hermes_tool_parser.py:108] ^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lse, "return_sql": false}}} ``` Here is how I start vllm service: ``` docker run --runtime nvidia --gpus='"device=4,5,6,7"' \ --mount type=bind,source=/home/llm,target=/llm \ -p 7415:8000 \ --ipc=host \ vllm/vllm-openai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: mes_tool_parser.py:108] Error in extracting tool call from response. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This error occurred when I used the Qwen2.5-72B-AWQ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t1` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tool call from response. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This error occurred when I used the Qwen2.5-72B-AWQ model to make tool calls (with `stream=False...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
