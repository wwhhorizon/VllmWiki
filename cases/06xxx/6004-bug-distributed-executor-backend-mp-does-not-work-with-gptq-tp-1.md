# vllm-project/vllm#6004: [Bug]: `distributed_executor_backend=mp` does not work with GPTQ tp>1

| 字段 | 值 |
| --- | --- |
| Issue | [#6004](https://github.com/vllm-project/vllm/issues/6004) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;kernel;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `distributed_executor_backend=mp` does not work with GPTQ tp>1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug `distributed_executor_backed="mp"` is now enabled by default for vLLM. However, this feature is currently incompatible with some GPTQ quantization for tp>1 due to the order in which torch is initialized. We get the classic `RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method` Setting `distributed_backend_executor="ray"` works for GPTQ The following fails: ```python from vllm import LLM MODEL_NAME="TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ" TENSOR_PARALLEL_SIZE=2 model = LLM(MODEL_NAME, enforce_eager=True, tensor_parallel_size=TENSOR_PARALLEL_SIZE, distributed_executor_backend="mp") print(model.generate("The best thing about the internet is")[0].outputs[0].text) ``` with: ```bash (vllm-upstream) rshaw@beaker:~/vllm$ python3 run.py INFO 06-30 14:26:18 gptq_marlin.py:140] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. INFO 06-30 14:26:18 llm_engine.py:169] Initializing an LLM engine (v0.5.0.post1) with config: model='TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ', speculative_co...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: for vLLM. However, this feature is currently incompatible with some GPTQ quantization for tp>1 due to the order in which torch is initialized. We get the classic `RuntimeError: Cannot re-initialize CUDA in forked subpro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: y"` works for GPTQ The following fails: ```python from vllm import LLM MODEL_NAME="TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ" TENSOR_PARALLEL_SIZE=2 model = LLM(MODEL_NAME, enforce_eager=True, tensor_parallel_size=TENSOR_P...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: executor="ray"` works for GPTQ The following fails: ```python from vllm import LLM MODEL_NAME="TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ" TENSOR_PARALLEL_SIZE=2 model = LLM(MODEL_NAME, enforce_eager=True, tensor_parallel_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h is initialized. We get the classic `RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method` Setting `distributed_backend_executor="ray"` w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: `distributed_executor_backend=mp` does not work with GPTQ tp>1 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug `distributed_executor_backed="mp"` is now e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
