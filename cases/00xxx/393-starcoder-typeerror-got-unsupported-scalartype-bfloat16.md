# vllm-project/vllm#393: [StarCoder] TypeError: Got unsupported ScalarType BFloat16

| 字段 | 值 |
| --- | --- |
| Issue | [#393](https://github.com/vllm-project/vllm/issues/393) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [StarCoder] TypeError: Got unsupported ScalarType BFloat16

### Issue 正文摘录

Unable to run StarCoder inference in BFloat16 precision with the following error message: ``` RayActorError: The actor died because of an error raised in its creation task, [36mray::LLMEngine.__init__()[39m (pid=159533, ip=, actor_id=1eb9d05287fc2a9a9826284701000000, repr= ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/one/anaconda3/envs/torch/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 105, in __init__ self._init_cache() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/one/anaconda3/envs/torch/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 117, in _init_cache num_blocks = self._run_workers( ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/one/anaconda3/envs/torch/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 334, in _run_workers all_outputs = ray.get(all_outputs) ^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ray.exceptions.RayActorError: The actor died because of an error raised in its creation task, [36mray::Worker.__init__()[39m (pid=159651, ip=, actor_id=8315997dcbcb3ad9006b2db801000000, repr= ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [StarCoder] TypeError: Got unsupported ScalarType BFloat16 bug Unable to run StarCoder inference in BFloat16 precision with the following error message: ``` RayActorError: The actor died because of an error raised in it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 3.11/site-packages/vllm/worker/worker.py", line 45, in __init__ self.model = get_model(model_config) ^^^^^^^^^^^^^^^^^^^^^^^ File "/home/one/anaconda3/envs/torch/lib/python3.11/site-packages/vllm/model_executor/model_lo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ed ScalarType BFloat16 bug Unable to run StarCoder inference in BFloat16 precision with the following error message: ``` RayActorError: The actor died because of an error raised in its creation task, [36mray::LLMEngine....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ScalarType BFloat16 bug Unable to run StarCoder inference in BFloat16 precision with the following error message: ``` RayActorError: The actor died because of an error raised in its creation task, [36mray::LLMEngine.__i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: te-packages/vllm/engine/llm_engine.py", line 117, in _init_cache num_blocks = self._run_workers( ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/one/anaconda3/envs/torch/lib/python3.11/site-packages/vllm/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
