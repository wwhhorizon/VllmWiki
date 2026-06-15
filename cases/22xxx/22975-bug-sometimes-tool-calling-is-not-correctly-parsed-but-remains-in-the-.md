# vllm-project/vllm#22975: [Bug]: sometimes tool calling is not correctly parsed but remains in the plain content for qwen3 coder

| 字段 | 值 |
| --- | --- |
| Issue | [#22975](https://github.com/vllm-project/vllm/issues/22975) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sometimes tool calling is not correctly parsed but remains in the plain content for qwen3 coder

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For some requests to qwen3 coder, I can get responses like this, where the tool calling is not correctly parsed as tool calls: ```python vllm/vllm-openai latest 4d3b60090244 2 weeks ago 21.2GB docker run --runtime nvidia --gpus all --shm-size 32g -it --rm \ --network=host \ --ipc=host \ -v /ssd/share/huggingface:/root/.cache/huggingface \ --name vllm_qwen3 \ vllm/vllm-openai:latest \ --model Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \ --trust-remote-code \ --host 0.0.0.0 --port 30008 \ --tensor-parallel-size 4 --data-parallel-size 2 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --enable-expert-parallel ModelResponse(id='chatcmpl-66e83c6c9b2047519d4815483d85dbda', created=1755245218, model='Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content="Let me check if there might be a base.py file that's not showing up. Since we know it's being imported, let me try to grep for the implementation of BaseService.\n\n \n \n \nclass BaseService\\(\n \n \n.\n \n \n ", role='assistant', tool_calls=None, function_call=Non...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: thon vllm/vllm-openai latest 4d3b60090244 2 weeks ago 21.2GB docker run --runtime nvidia --gpus all --shm-size 32g -it --rm \ --network=host \ --ipc=host \ -v /ssd/share/huggingface:/root/.cache/huggingface \ --name vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm/vllm-openai:latest \ --model Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \ --trust-remote-code \ --host 0.0.0.0 --port 30008 \ --tensor-parallel-size 4 --data-parallel-size 2 \ --enable-auto-tool-choice \ --tool-call-pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ool calling is not correctly parsed but remains in the plain content for qwen3 coder bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug For some requests to qwen3 coder, I can get responses like...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ot correctly parsed but remains in the plain content for qwen3 coder bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug For some requests to qwen3 coder, I can get responses like this, where the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
