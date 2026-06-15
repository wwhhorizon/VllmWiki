# vllm-project/vllm#9922: [Bug]: ValueError: XFormers does not support attention logits soft capping for GPU Quadro RTX 4000

| 字段 | 值 |
| --- | --- |
| Issue | [#9922](https://github.com/vllm-project/vllm/issues/9922) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 | crash |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: XFormers does not support attention logits soft capping for GPU Quadro RTX 4000

### Issue 正文摘录

### Your current environment vllm version: 0.6.3.post1 gpu type: Quadro RTX 4000 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I try to use gamme series such as `google/gemma-2-27b-it` in the vllm offline batch inference, but it seems that gemma is not supported for this GPU type ? any other methods to solve it ? thanks. > [rank0]: Traceback (most recent call last): > [rank0]: File "/home/yanan/test_vllm.py", line 11, in > [rank0]: llm = LLM(model= args.llm_name, dtype='half', max_model_len= 4096, > [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ > [rank0]: File "/home/yanan/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 177, in __init__ > [rank0]: self.llm_engine = LLMEngine.from_engine_args( > [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ > [rank0]: File "/home/yanan/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 573, in from_engine_args > [rank0]: engine = cls( > [rank0]: ^^^^ > [rank0]: File "/home/yanan/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 334, in __init__ > [rank0]: self.model_executor = executor_class( > [rank0]: ^^^^^^^^^^^^^^^ > [rank0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t environment vllm version: 0.6.3.post1 gpu type: Quadro RTX 4000 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I try to use gamme series such as `google/gemma-2-27b-it` in the vllm offline batch inference,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t_vllm.py", line 11, in > [rank0]: llm = LLM(model= args.llm_name, dtype='half', max_model_len= 4096, > [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ > [rank0]: File "/home/yanan/anaconda3/envs/v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t capping for GPU Quadro RTX 4000 bug ### Your current environment vllm version: 0.6.3.post1 gpu type: Quadro RTX 4000 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I try to use gamme series such as `google...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : XFormers does not support attention logits soft capping for GPU Quadro RTX 4000 bug ### Your current environment vllm version: 0.6.3.post1 gpu type: Quadro RTX 4000 ### Model Input Dumps _No response_ ### 🐛 Describe t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: me/yanan/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/attention/backends/xformers.py", line 425, in __init__ > [rank0]: raise ValueError( > [rank0]: ValueError: XFormers does not support attention logits soft c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
