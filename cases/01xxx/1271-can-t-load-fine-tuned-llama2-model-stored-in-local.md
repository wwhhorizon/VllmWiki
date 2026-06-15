# vllm-project/vllm#1271: Can't load fine-tuned LLama2 model stored in local

| 字段 | 值 |
| --- | --- |
| Issue | [#1271](https://github.com/vllm-project/vllm/issues/1271) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Can't load fine-tuned LLama2 model stored in local

### Issue 正文摘录

I have a fine-tuned LLama2 model (LoRA Layers merged). Model folder contains following files: - config.json - generation_config.json - model-00001-of-00002.safetensors - model-00002-of-00002.safetensors - model.safetensors.index.json - special_tokens_map.json - tokenizer_config.json - tokenizer.json When I try to load the model it throws following error. Any idea on how to resolve this? `llm = LLM(model="./llama-ft/merged_model")` > --------------------------------------------------------------------------- > AssertionError Traceback (most recent call last) > Cell In[16], line 11 > 3 prompts = [ > 4 "Hello, my name is", > 5 "The president of the United States is", > 6 "The capital of France is", > 7 "The future of AI is", > 8 ] > 9 sampling_params = SamplingParams(temperature=0.8, top_p=0.95) > ---> 11 llm = LLM(model="./llama-ft/merged_model") > > File /opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py:89, in LLM.__init__(self, model, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, seed, gpu_memory_utilization, swap_space, **kwargs) > 74 kwargs["disable_log_stats"] = True > 75 engine_args = EngineArgs( > 76 model=mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: - model-00002-of-00002.safetensors - model.safetensors.index.json - special_tokens_map.json - tokenizer_config.json - tokenizer.json When I try to load the model it throws following error. Any idea on how to resolve thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Can't load fine-tuned LLama2 model stored in local I have a fine-tuned LLama2 model (LoRA Layers merged). Model folder contains following files: - config.json - generation_config.json - model-00001-of-00002.safetensors...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, seed, gpu_memory_utilization, swap_space, **kwargs) > 74 kwargs["disable_log_stats"] = True > 75 engine_args = Engi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ges/vllm/worker/worker.py:63, in Worker.init_model(self) > 60 torch.cuda.set_device(self.device) > 62 # Initialize the distributed environment. > ---> 63 _init_distributed_environment(self.parallel_config, self.rank, >...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: self.llm_engine = LLMEngine.from_engine_args(engine_args) > 90 self.request_counter = Counter() > > File /opt/conda/lib/python3.10/site-packages/vllm/engine/llm_engine.py:229, in LLMEngine.from_engine_args(cls, engine_a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
