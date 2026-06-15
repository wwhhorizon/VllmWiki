# vllm-project/vllm#3813: [Bug]: AssertionError when load miqu70b after full sft

| 字段 | 值 |
| --- | --- |
| Issue | [#3813](https://github.com/vllm-project/vllm/issues/3813) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError when load miqu70b after full sft

### Issue 正文摘录

### Your current environment environment pip install auto_gptq modelscope xformers torchvision torchaudio torch==2.1.2 -U pip install datasets huggingface-hub transformers==4.39.1 -U pip install fastrlock cupy-cuda11x==12.1.0 pip install flash_attn==2.5.6 pip install vllm==0.4.0 ### 🐛 Describe the bug When I load miqu-70b model after full sft（node: 4, nproc_per_node: 8）, the following error occurs: llm = LLM(model=args.ckpt_dir, trust_remote_code=True, seed=42, tensor_parallel_size=torch.cuda.device_count()) File "/home/jeeves/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 112, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/home/jeeves/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 196, in from_engine_args engine = cls( File "/home/jeeves/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 110, in __init__ self.model_executor = executor_class(model_config, cache_config, File "/home/jeeves/.local/lib/python3.10/site-packages/vllm/executor/ray_gpu_executor.py", line 62, in __init__ self._init_workers_ray(placement_group) File "/home/jeeves/.local/lib/python3.10/site-packages/vllm/executor/ray_gpu_executor.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: miqu70b after full sft bug ### Your current environment environment pip install auto_gptq modelscope xformers torchvision torchaudio torch==2.1.2 -U pip install datasets huggingface-hub transformers==4.39.1 -U pip insta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sft bug ### Your current environment environment pip install auto_gptq modelscope xformers torchvision torchaudio torch==2.1.2 -U pip install datasets huggingface-hub transformers==4.39.1 -U pip install fastrlock cupy-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: asets huggingface-hub transformers==4.39.1 -U pip install fastrlock cupy-cuda11x==12.1.0 pip install flash_attn==2.5.6 pip install vllm==0.4.0 ### 🐛 Describe the bug When I load miqu-70b model after full sft（node: 4, np...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: :49 ray_utils.py:44] Error executing method load_model. This might cause deadlock in distributed execution. [36m(RayWorkerVllm pid=1135)[0m ERROR 04-03 14:52:49 ray_utils.py:44] Traceback (most recent call last): [36...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
