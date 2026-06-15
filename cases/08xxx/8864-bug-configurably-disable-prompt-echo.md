# vllm-project/vllm#8864: [Bug]: configurably disable prompt echo

| 字段 | 值 |
| --- | --- |
| Issue | [#8864](https://github.com/vllm-project/vllm/issues/8864) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: configurably disable prompt echo

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using vLLM, the returned text always also includes the prompt itself. This is great for batching but sometimes sub-optimal Please add a flag that when configured will prevents the prompt from echoing (possibly only when not streaming) The analogue Gradio flag would be return_full_text=False Here is a crude patch to force a fix diff --git a/vllm/entrypoints/api_server.py b/vllm/entrypoints/api_server.py index f3e80cab..07c3807a 100644 --- a/vllm/entrypoints/api_server.py +++ b/vllm/entrypoints/api_server.py @@ -63,7 +63,7 @@ async def generate(request: Request) -> Response: prompt = request_output.prompt assert prompt is not None text_outputs = [ `- prompt + output.text for output in request_output.outputs` `+ prompt*0 + output.text for output in request_output.outputs` ] ret = {"text": text_outputs} yield (json.dumps(ret) + "\0").encode("utf-8") @@ -82,7 +82,7 @@ async def generate(request: Request) -> Response: assert final_output is not None prompt = final_output.prompt assert prompt is not None `- text_outputs = [prompt + output.text for output in final_output.outputs]` `+ text_outputs...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: configurably disable prompt echo bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using vLLM, the returned text always also includes the prompt itself. This is
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: configurably disable prompt echo bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using vLLM, the returned text always also includes the prompt itself. This i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: et) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: when not streaming) The analogue Gradio flag would be return_full_text=False Here is a crude patch to force a fix diff --git a/vllm/entrypoints/api_server.py b/vllm/entrypoints/api_server.py index f3e80cab..07c3807a 100...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
