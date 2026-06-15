# vllm-project/vllm#14650: [Bug]: TPU Ray Actor Hangs on Initialization for Multi-node with local directory

| 字段 | 值 |
| --- | --- |
| Issue | [#14650](https://github.com/vllm-project/vllm/issues/14650) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TPU Ray Actor Hangs on Initialization for Multi-node with local directory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using the docker image: vllm/vllm-tpu:e92694b6fe264a85371317295bca6643508034ef My process hangs when I try to run distributed inference on a TPU v4-16 which should have 8 TPUs. However, I noticed that if I run it with just the function and NOT the actor, it works. It makes me believe that there's something wrong with the way that the TPU actor in Ray communicates with the other host? So, it fails to connect. The error I get is after 30 minutes, I get a torch timeout that says RESOURCE_EXHAUSTED. I'm assuming this is related to the timeout for communication. However, this works when I use the huggingface path: meta-llama/Llama-3.1-8B-Instruct. Error (hanging): ``` (LLMActor pid=14079, ip=10.130.0.111) INFO 03-12 01:46:17 config.py:543] This model supports multiple tasks: {'reward', 'score', 'classify', 'generate', 'embed'}. Defaulting to 'generate'. (LLMActor pid=14079, ip=10.130.0.111) INFO 03-12 01:46:17 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3.dev86+ge92694b6) with config: model='/opt/gcsfuse_mount/models/meta-llama--Llama-3-1-8B-Instruct', speculative_config=None, tokenizer='/opt/gcsfuse_mount/models/meta-ll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: e ### Your current environment ### 🐛 Describe the bug I'm using the docker image: vllm/vllm-tpu:e92694b6fe264a85371317295bca6643508034ef My process hangs when I try to run distributed inference on a TPU v4-16 which shou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ted to the timeout for communication. However, this works when I use the huggingface path: meta-llama/Llama-3.1-8B-Instruct. Error (hanging): ``` (LLMActor pid=14079, ip=10.130.0.111) INFO 03-12 01:46:17 config.py:543]...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_all_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ig={"level":2,"backend":"openxla","splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, (LLMActor pid=14079, ip=10.130.0.111) WARNING 03-12 01:46:18 ray_util...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ay Actor Hangs on Initialization for Multi-node with local directory bug;stale ### Your current environment ### 🐛 Describe the bug I'm using the docker image: vllm/vllm-tpu:e92694b6fe264a85371317295bca6643508034ef My pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
