# vllm-project/vllm#16448: [Bug]: Load meta-llama/Llama-3.2-1B-Instruct throw error: ValueError: Cannot cast <zmq.Socket(zmq.ROUTER) at 0x784ecf7f4940> to int

| 字段 | 值 |
| --- | --- |
| Issue | [#16448](https://github.com/vllm-project/vllm/issues/16448) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Load meta-llama/Llama-3.2-1B-Instruct throw error: ValueError: Cannot cast <zmq.Socket(zmq.ROUTER) at 0x784ecf7f4940> to int

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the following code: ``` from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.2-1B-Instruct") ``` throw error: ``` --------------------------------------------------------------------------- ValueError Traceback (most recent call last) Cell In[3], [line 1](vscode-notebook-cell:?execution_count=3&line=1) ----> [1](vscode-notebook-cell:?execution_count=3&line=1) llm = LLM(model="meta-llama/Llama-3.2-1B-Instruct") File /workspace/vllm/vllm/utils.py:1097, in deprecate_args. .wrapper. .inner(*args, **kwargs) [1090](https://vscode-remote+ssh-002dremote-002b87-002e197-002e146-002e56.vscode-resource.vscode-cdn.net/workspace/vllm/vllm/utils.py:1090) msg += f" {additional_message}" [1092](https://vscode-remote+ssh-002dremote-002b87-002e197-002e146-002e56.vscode-resource.vscode-cdn.net/workspace/vllm/vllm/utils.py:1092) warnings.warn( [1093](https://vscode-remote+ssh-002dremote-002b87-002e197-002e146-002e56.vscode-resource.vscode-cdn.net/workspace/vllm/vllm/utils.py:1093) DeprecationWarning(msg), [1094](https://vscode-remote+ssh-002dremote-002b87-002e197-002e146-002e56.vscode-resource.vscode-cdn.net/workspace/vllm/v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ent ### 🐛 Describe the bug I run the following code: ``` from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.2-1B-Instruct") ``` throw error: ``` ----------------------------------------------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Load meta-llama/Llama-3.2-1B-Instruct throw error: ValueError: Cannot cast <zmq.Socket(zmq.ROUTER) at 0x784ecf7f4940> to int bug ### Your current environment ### 🐛 Describe the bug I run the following code: ``` f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: resource.vscode-cdn.net/workspace/vllm/vllm/entrypoints/llm.py:252) self.request_counter = Counter() File /workspace/vllm/vllm/engine/llm_engine.py:522, in LLMEngine.from_engine_args(cls, engine_args, usage_context, sta...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: init, trust_remote_code, allowed_local_media_path, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
