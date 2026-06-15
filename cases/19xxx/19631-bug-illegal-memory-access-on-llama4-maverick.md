# vllm-project/vllm#19631: [Bug]: Illegal memory access on llama4 maverick

| 字段 | 值 |
| --- | --- |
| Issue | [#19631](https://github.com/vllm-project/vllm/issues/19631) |
| 状态 | closed |
| 标签 | bug;torch.compile;llama |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Illegal memory access on llama4 maverick

### Issue 正文摘录

### Your current environment PyTorch 2.7.0, vLLM main branch built from source. ### 🐛 Describe the bug Repro: ```py vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --tensor-parallel-size 8 --max-num-batched-tokens 40000 --max-model-len 8192 --max-num-seqs 128 --gpu-memory-utilization 0.8 ``` gives a CUDA Illegal Memory Access, as well as some errors: ``` ERROR 06-13 15:32:09 [core.py:515] EngineCore failed to start. ERROR 06-13 15:32:09 [core.py:515] Traceback (most recent call last): ERROR 06-13 15:32:09 [core.py:515] File "/home/rzou/dev/stable0/vllm-stable0/vllm/v1/engine/core.py", line 506, in run_engine_core ERROR 06-13 15:32:09 [core.py:515] engine_core = EngineCoreProc(*args, **kwargs) ERROR 06-13 15:32:09 [core.py:515] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-13 15:32:09 [core.py:515] File "/home/rzou/dev/stable0/vllm-stable0/vllm/v1/engine/core.py", line 390, in __init__ ERROR 06-13 15:32:09 [core.py:515] super().__init__(vllm_config, executor_class, log_stats, ERROR 06-13 15:32:09 [core.py:515] File "/home/rzou/dev/stable0/vllm-stable0/vllm/v1/engine/core.py", line 83, in __init__ ERROR 06-13 15:32:09 [core.py:515] self._initialize_kv_caches(vllm_config) ERR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Illegal memory access on llama4 maverick bug;torch.compile;llama ### Your current environment PyTorch 2.7.0, vLLM main branch built from source. ### 🐛 Describe the bug Repro: ```py vllm serve meta-llama/Llama-4-M...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g Repro: ```py vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --tensor-parallel-size 8 --max-num-batched-tokens 40000 --max-model-len 8192 --max-num-seqs 128 --gpu-memory-utilization 0.8 ``` gives a CUDA I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: del-len 8192 --max-num-seqs 128 --gpu-memory-utilization 0.8 ``` gives a CUDA Illegal Memory Access, as well as some errors: ``` ERROR 06-13 15:32:09 [core.py:515] EngineCore failed to start. ERROR 06-13 15:32:09 [core....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: or: Worker failed with error 'Expected result >= 0 to be true, but got false. (Could this error message be improved? If so, please report an enhancement request to PyTorch.)', please check the stack trace above for the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Illegal memory access on llama4 maverick bug;torch.compile;llama ### Your current environment PyTorch 2.7.0, vLLM main branch built from source. ### 🐛 Describe the bug Repro: ```py vllm serve meta-llama/Llama-4-M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
