# vllm-project/vllm#2856: [0.2.7] LLAMA 70B AWQ OOM with TP8

| 字段 | 值 |
| --- | --- |
| Issue | [#2856](https://github.com/vllm-project/vllm/issues/2856) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [0.2.7] LLAMA 70B AWQ OOM with TP8

### Issue 正文摘录

Hi there, I was testing with AWS G5.48xl machine with A10G GPU (24GB each). ``` llm = LLM(model="TheBloke/Llama-2-70B-AWQ, quantization='awq', dtype='half', tensor_parallel_size=8) ``` And This result to OOM. However, TP4 works fine with it: ``` llm = LLM(model="TheBloke/Llama-2-70B-AWQ, quantization='awq', dtype='half', tensor_parallel_size=4) ``` Not sure what could be the cause, since more GPUs should have more memory bandwidth ## Logs ``` WARN PyProcess W-252-model-stderr: 2024-02-13 20:43:43,457 ERROR worker.py:405 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerVllm.execute_method() (pid=10548, ip=172.17.0.2, actor_id=52763143f84a75fbe7e8dca001000000, repr= ) WARN PyProcess W-252-model-stderr: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/ray_utils.py", line 30, in execute_method WARN PyProcess W-252-model-stderr: return executor(*args, **kwargs) WARN PyProcess W-252-model-stderr: File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker.py", line 125, in warm_up_model WARN PyProcess W-252-model-stderr: self.model_runner.capture_model(self.gpu_cache) WARN PyProcess W-252-model-stderr: File "/usr/local/lib/python3.10/dist-p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ider passing CUDA_LAUNCH_BLOCKING=1. WARN PyProcess W-252-model-stderr: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` correctness ci_build;distributed_parallel;frontend_api;model_support;quanti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: th A10G GPU (24GB each). ``` llm = LLM(model="TheBloke/Llama-2-70B-AWQ, quantization='awq', dtype='half', tensor_parallel_size=8) ``` And This result to OOM. However, TP4 works fine with it: ``` llm = LLM(model="TheBlok...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: line 580, in capture WARN PyProcess W-252-model-stderr: with torch.cuda.graph(self.graph, pool=memory_pool): WARN PyProcess W-252-model-stderr: File "/usr/local/lib/python3.10/dist-packages/torch/cuda/graphs.py", line 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [0.2.7] LLAMA 70B AWQ OOM with TP8 Hi there, I was testing with AWS G5.48xl machine with A10G GPU (24GB each). ``` llm = LLM(model="TheBloke/Llama-2-70B-AWQ, quantization='awq', dtype='half', tensor_parallel_size=8) ```...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pport;quantization;scheduler_memory cuda;kernel;quantization build_error;mismatch;oom dtype;env_dependency Hi there,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
