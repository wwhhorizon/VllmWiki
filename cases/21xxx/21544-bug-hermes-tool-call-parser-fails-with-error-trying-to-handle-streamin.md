# vllm-project/vllm#21544: [Bug]: Hermes tool call parser fails with "Error trying to handle streaming tool call"

| 字段 | 值 |
| --- | --- |
| Issue | [#21544](https://github.com/vllm-project/vllm/issues/21544) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Hermes tool call parser fails with "Error trying to handle streaming tool call"

### Issue 正文摘录

### Your current environment This model is deployed on 8xH200 and vllm 0.9.2. Not easy for me to run collect_env unfortunately. ``` - '--model=Qwen--Qwen3-Coder-480B-A35B-Instruct' - '--distributed-executor-backend=ray' - '--load-format=runai_streamer' - '--port=5000' - '--tensor-parallel-size=8' - '--served-model-name=Qwen3-Coder-480B-A35B-Instruct' - '--uvicorn-log-level=warning' - '--block_size=32' - '--gpu-memory-utilization=0.90' - '--max-model-len=200000' - '--max-num-seqs=1024' - '--enable-expert-parallel' - '--enable-auto-tool-choice' - '--tool-call-parser=hermes' - '--enable-prefix-caching' - '--max-num-batched-tokens=4096' - '--dtype=bfloat16' ``` ### 🐛 Describe the bug This happened when i used the qwen-code cli, pointed it towards the openai api server and prompted: ``` Run command mkdir -p test/{test1,test2 ``` I know the command itself makes no sense, but that seems to break the tool call parser. Logs: ```text ERROR 07-24 10:16:06 [hermes_tool_parser.py:370] Traceback (most recent call last): ERROR 07-24 10:16:06 [hermes_tool_parser.py:370] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py", line 241, in extract_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rmes' - '--enable-prefix-caching' - '--max-num-batched-tokens=4096' - '--dtype=bfloat16' ``` ### 🐛 Describe the bug This happened when i used the qwen-code cli, pointed it towards the openai api server and prompted: ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng to handle streaming tool call" bug ### Your current environment This model is deployed on 8xH200 and vllm 0.9.2. Not easy for me to run collect_env unfortunately. ``` - '--model=Qwen--Qwen3-Coder-480B-A35B-Instruct'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: '--model=Qwen--Qwen3-Coder-480B-A35B-Instruct' - '--distributed-executor-backend=ray' - '--load-format=runai_streamer' - '--port=5000' - '--tensor-parallel-size=8' - '--served-model-name=Qwen3-Coder-480B-A35B-Instruct'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ame=Qwen3-Coder-480B-A35B-Instruct' - '--uvicorn-log-level=warning' - '--block_size=32' - '--gpu-memory-utilization=0.90' - '--max-model-len=200000' - '--max-num-seqs=1024' - '--enable-expert-parallel' - '--enable-auto-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
