# vllm-project/vllm#10284: [Misc]: Invariant encountered: value was None when it should not be

| 字段 | 值 |
| --- | --- |
| Issue | [#10284](https://github.com/vllm-project/vllm/issues/10284) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | debug |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Invariant encountered: value was None when it should not be

### Issue 正文摘录

I am working on a use case of loading a model with parallel gpus, then unloading the model, and loading a new model in the same process. ``` @classmethod async def unload_models(cls, exiting=False) -> None: try: if cls._loaded_models: logging.info("log: unloading all cached models.") torch.multiprocessing.set_start_method("spawn", force=True) destroy_model_parallel() for model_id in list(cls._loaded_models.keys()): del cls._loaded_models[model_id].llm_engine del cls._loaded_models[model_id] gc.collect() torch.cuda.empty_cache() torch.distributed.destroy_process_group() ``` although, when i use only 1 gpu this works, but when tensor_parallel_size is 2 or greater, its giving me the following error once the new model is being loaded: ``` 2024-11-12 22:16:18 - [INFO] - log: unloading all cached models. INFO 11-12 22:16:19 multiproc_worker_utils.py:133] Terminating local vLLM worker processes (VllmWorkerProcess pid=3574636) INFO 11-12 22:16:19 multiproc_worker_utils.py:240] Worker exiting [rank1]:[W1112 22:16:20.271056884 CudaIPCTypes.cpp:16] Producer process has been terminated before all shared CUDA tensors released. See Note [Sharing CUDA tensors] 2024-11-12 22:16:24 - [INFO] - log:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Misc]: Invariant encountered: value was None when it should not be stale I am working on a use case of loading a model with parallel gpus, then unloading the model, and loading a new model in the same process. ``` @cla...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 0.6.3.post1) with config: model='neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8', speculative_config=None, tokenizer='neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8', skip_tokenizer_init=False, tokenizer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: None when it should not be stale I am working on a use case of loading a model with parallel gpus, then unloading the model, and loading a new model in the same process. ``` @classmethod async def unload_models(cls, exi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: worker_utils.py:133] Terminating local vLLM worker processes ``` in specific: Invariant encountered: value was None when it should not be I have tried everything I can find online - do you have any suggestions? your ins...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: oading the model, and loading a new model in the same process. ``` @classmethod async def unload_models(cls, exiting=False) -> None: try: if cls._loaded_models: logging.info("log: unloading all cached models.") torch.mu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
