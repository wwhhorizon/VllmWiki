# vllm-project/vllm#13603: [Bug]: When using cpu inference, is the kv cache's physical memory space pre-allocated?

| 字段 | 值 |
| --- | --- |
| Issue | [#13603](https://github.com/vllm-project/vllm/issues/13603) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using cpu inference, is the kv cache's physical memory space pre-allocated?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I read the papers in PagedAttention, which mentions that in inference, kv cache's physical memory size is being allocated at the time tokens are generated, and not pre-allocated. However, when I looked at the source code of vllm, I found that warm up pre-filled all kv cache in advance when reasoning on cpu, resulting in a large cpu memory consumption at the beginning of reasoning. Why does the description of the article not correspond to the source code? vllm cpu inference code is that: def _init_cache_engine(self) -> None: self.cache_engine = [ CPUCacheEngine(self.cache_config, self.model_config, self.parallel_config, self.device_config) for _ in range(self.parallel_config.pipeline_parallel_size) ] self.cpu_cache = [ self.cache_engine[ve].cpu_cache for ve in range(self.parallel_config.pipeline_parallel_size) ] bind_kv_cache(self.compilation_config.static_forward_context, self.cpu_cache) self.model_runner.block_size = self.cache_engine[0].block_size assert all( self.cpu_cache[ve] is not None for ve in range(self.parallel_config.pipeline_parallel_size)) # Populate the cache to warmup the memory for ve in range(self.parallel_config...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cache;cuda;operator;sampling build_error;nan_inf env_depend...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pu inference, is the kv cache's physical memory space pre-allocated? bug;stale ### Your current environment ### 🐛 Describe the bug I read the papers in PagedAttention, which mentions that in inference, kv cache's physic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: age ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: one: self.cache_engine = [ CPUCacheEngine(self.cache_config, self.model_config, self.parallel_config, self.device_config) for _ in range(self.parallel_config.pipeline_parallel_size) ] self.cpu_cache = [ sel
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: When using cpu inference, is the kv cache's physical memory space pre-allocated? bug;stale ### Your current environment ### 🐛 Describe the bug I read the papers in PagedAttention, which mentions that in inference...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
