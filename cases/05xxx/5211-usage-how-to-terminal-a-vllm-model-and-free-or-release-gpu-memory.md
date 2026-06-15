# vllm-project/vllm#5211: [Usage]: how to terminal a vllm model and free or release gpu memory

| 字段 | 值 |
| --- | --- |
| Issue | [#5211](https://github.com/vllm-project/vllm/issues/5211) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to terminal a vllm model and free or release gpu memory

### Issue 正文摘录

### Your current environment ```text def destroy(self): import gc import torch import ray import contextlib logger.info("vllm destroy") def cleanup(): from vllm.distributed.parallel_state import destroy_model_parallel # from vllm.model_executor.parallel_utils.parallel_state import destroy_model_parallel os.environ["TOKENIZERS_PARALLELISM"] = "false" destroy_model_parallel() with contextlib.suppress(AssertionError): torch.distributed.destroy_process_group() gc.collect() torch.cuda.empty_cache() ray.shutdown() for _ in range(10): cleanup() del self.model.llm_engine.model_executor.driver_worker del self.model gc.collect() torch.cuda.empty_cache() ``` vllm=0.4.2 I tried this method, but it didn't work. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ale ### Your current environment ```text def destroy(self): import gc import torch import ray import contextlib logger.info("vllm destroy") def cleanup(): from vllm.distributed.parallel_state import destroy_model_parall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mport destroy_model_parallel os.environ["TOKENIZERS_PARALLELISM"] = "false" destroy_model_parallel() with contextlib.suppress(AssertionError): torch.distributed.destroy_process_group() gc.collect() torch.cuda.empty_ca
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: how to terminal a vllm model and free or release gpu memory usage;stale ### Your current environment ```text def destroy(self): import gc import torch import ray import contextlib logger.info("vllm destroy") de...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: roy_model_parallel os.environ["TOKENIZERS_PARALLELISM"] = "false" destroy_model_parallel() with contextlib.suppress(AssertionError): torch.distributed.destroy_process_group() gc.collect() torch.cuda.empty_cache()
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: how to terminal a vllm model and free or release gpu memory usage;stale ### Your current environment ```text def destroy(self): import gc import torch import ray import contextlib logger.info("vllm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
