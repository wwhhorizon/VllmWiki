# vllm-project/vllm#2020: Mixtral - KeyError: 'model.layers.10.block_sparse_moe.experts.0.w1.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#2020](https://github.com/vllm-project/vllm/issues/2020) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral - KeyError: 'model.layers.10.block_sparse_moe.experts.0.w1.weight'

### Issue 正文摘录

Hello, I've installed vLLM from source with CUDA 12.1 and it is failing to instantiate the Mixtral model (I've tested both official models released by Mistral `mistralai/Mixtral-8x7B-Instruct-v0.1` and `mistralai/Mixtral-8x7B-v0.1`. The hardware to run it: - 2 A100 - 80GB GPUs The code I'm using to run it: ```python from vllm import LLM llm = LLM(model="mistralai/Mixtral-8x7B-v0.1", tensor_parallel_size=2) ``` Error stack trace: ``` RayTaskError(KeyError) Traceback (most recent call last) Cell In[2], line 1 ----> 1 llm = LLM(model="mistralai/Mixtral-8x7B-v0.1", tensor_parallel_size=2) File /opt/conda/lib/python3.11/site-packages/vllm/entrypoints/llm.py:93, in LLM.__init__(self, model, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, **kwargs) 77 kwargs["disable_log_stats"] = True 78 engine_args = EngineArgs( 79 model=model, 80 tokenizer=tokenizer, (...) 91 **kwargs, 92 ) ---> 93 self.llm_engine = LLMEngine.from_engine_args(engine_args) 94 self.request_counter = Counter() File /opt/conda/lib/python3.11/site-packages/vllm/engine/llm_engine.py:246, in LLMEngine.from_engine_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ror: 'model.layers.10.block_sparse_moe.experts.0.w1.weight' Hello, I've installed vLLM from source with CUDA 12.1 and it is failing to instantiate the Mixtral model (I've tested both official models released by Mistral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, **kwargs) 77 kwargs["disable_log_stats"] = True 78 en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se_moe.experts.0.w1.weight' Hello, I've installed vLLM from source with CUDA 12.1 and it is failing to instantiate the Mixtral model (I've tested both official models released by Mistral `mistralai/Mixtral-8x7B-Instruct...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Mixtral - KeyError: 'model.layers.10.block_sparse_moe.experts.0.w1.weight' Hello, I've installed vLLM from source with CUDA 12.1 and it is failing to instantiate the Mixtral model (I've tested both official models relea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Mixtral - KeyError: 'model.layers.10.block_sparse_moe.experts.0.w1.weight' Hello, I've installed vLLM from source with CUDA 12.1 and it is failing to instantiate the Mixtral model (I've tested both official models relea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
