# vllm-project/vllm#13707: [Bug]: vLLM Local path model loading error

| 字段 | 值 |
| --- | --- |
| Issue | [#13707](https://github.com/vllm-project/vllm/issues/13707) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM Local path model loading error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It's not really an error, but when I load from a local path, it complains that the repo name is not in the right format, but it is still able to load the model, which is sort of interesting. So, in other words, it basically works fine but has some extra logs that shouldn't be there? Min repro script (you can remove the ray components to run it locally): ``` import ray from vllm import LLM @ray.remote(resources={"TPU-v6e-8-head": 1, "TPU": 1}) def load_llm(): llm = LLM( model="/opt/gcsfuse_mount/models/meta-llama--Llama-3-1-8B-Instruct", ) return llm llm = load_llm.remote() ray.get(llm) ``` Error: ``` (pid=11741, ip=10.202.0.5) WARNING:root:libtpu.so and TPU device found. Setting PJRT_DEVICE=TPU. (load_llm pid=11741, ip=10.202.0.5) DEBUG 02-22 19:54:18 __init__.py:28] No plugins for group vllm.platform_plugins found. (load_llm pid=11741, ip=10.202.0.5) INFO 02-22 19:54:18 __init__.py:190] Automatically detected platform tpu. (load_llm pid=11741, ip=10.202.0.5) DEBUG 02-22 19:54:18 __init__.py:28] No plugins for group vllm.general_plugins found. (load_llm pid=11741, ip=10.202.0.5) --- Logging error --- (load_llm pid=11741, ip=10.20...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vLLM Local path model loading error bug;stale ### Your current environment ### 🐛 Describe the bug It's not really an error, but when I load from a local path, it complains that the repo name is not in the right f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vLLM Local path model loading error bug;stale ### Your current environment ### 🐛 Describe the bug It's not really an error, but when I load from a local path, it complains that the repo name is not in the right f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_al...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: repro script (you can remove the ray components to run it locally): ``` import ray from vllm import LLM @ray.remote(resources={"TPU-v6e-8-head": 1, "TPU": 1}) def load_llm(): llm = LLM( model="/opt/gcsfuse_mount/models/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the initial memory profiling phase, or result in low performance due to small KV cache space. Consider setting --max-model-len to a smaller value. (load_llm pid=11741, ip=10.202.0.5) INFO 02-22 19:54:23 llm_engine.py:23...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
