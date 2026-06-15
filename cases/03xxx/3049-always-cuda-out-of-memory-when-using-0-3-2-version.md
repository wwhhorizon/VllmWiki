# vllm-project/vllm#3049: Always CUDA out of memory when using 0.3.2 version

| 字段 | 值 |
| --- | --- |
| Issue | [#3049](https://github.com/vllm-project/vllm/issues/3049) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Always CUDA out of memory when using 0.3.2 version

### Issue 正文摘录

My vllm inference program runs well for most models with the environment of 'transformers=4.36.2' and 'vllm 0.2.7+cu118'. But when I update the two packages in an attempt to run inference with gemma-7b-it, all my attempts to run inference terminate with error like: ``` File "/cpfs01/user/liupengfei/jlli/anaconda3/envs/alignment_newest/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/cpfs01/user/liupengfei/jlli/anaconda3/envs/alignment_newest/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 371, in from_engine_args engine = cls(*engine_configs, File "/cpfs01/user/liupengfei/jlli/anaconda3/envs/alignment_newest/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 123, in __init__ self._init_cache() File "/cpfs01/user/liupengfei/jlli/anaconda3/envs/alignment_newest/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 357, in _init_cache self._run_workers("init_cache_engine", cache_config=self.cache_config) File "/cpfs01/user/liupengfei/jlli/anaconda3/envs/alignment_newest/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1014, in _run_workers driver_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ry when using 0.3.2 version My vllm inference program runs well for most models with the environment of 'transformers=4.36.2' and 'vllm 0.2.7+cu118'. But when I update the two packages in an attempt to run inference wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Always CUDA out of memory when using 0.3.2 version My vllm inference program runs well for most models with the environment of 'transformers=4.36.2' and 'vllm 0.2.7+cu118'. But when I update the two packages in an attem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Always CUDA out of memory when using 0.3.2 version My vllm inference program runs well for most models with the environment of 'transformers=4.36.2' and 'vllm 0.2.7+cu118'. But when I update the two packages in an attem...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: performance model_support;sampling_logits;scheduler_memory cuda;sampling oom env_dependency My vllm inference program runs well for most models with the environment of 'transformers=4.36.2' and 'vllm 0.2.7+cu118'. But w...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s/vllm/worker/cache_engine.py", line 84, in allocate_gpu_cache value_blocks = torch.empty( torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 926.00 MiB. GPU 0 has a total capacty of 79.35 GiB of which 8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
