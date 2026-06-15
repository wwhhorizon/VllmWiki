# vllm-project/vllm#7524: [Feature]: need a GB-based alternative for gpu_memory_utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#7524](https://github.com/vllm-project/vllm/issues/7524) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: need a GB-based alternative for gpu_memory_utilization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm struggling to figure out how to extend our test suite to include vllm tests. The problem is that by default vllm will take over the whole gpu, which prevents running multiple parallel tests with pytest-xdist - as all tests but on the first worker will fail with OOM. The tests use tiny models so running 4-6 tests in parallel on a 24GB gpu works just fine w/o vllm. Using `gpu_memory_utilization` isn't a solution because each test may require a specific amount of memory and it'd be very difficult to make the test suite efficient by doing a rough `gpu_memory_utilization=1/num_workers` because of cuda kernels and other various things and the possibility for the test suite run on different gpus of different sizes, as the tests run on CI with a certain gpu type and the developers use other gpu types when they develop the tests. The parallelization run would work well if each test could tell how much memory it needs via say a new config setting `gpu_memory_utilization_in_gbs` - it probably shouldn't be very complicated to add since `gpu_memory_utilization` already goes through the process of calculating the actual number of GBs it can use for it...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _memory_utilization` isn't a solution because each test may require a specific amount of memory and it'd be very difficult to make the test suite efficient by doing a rough `gpu_memory_utilization=1/num_workers` because...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: all tests but on the first worker will fail with OOM. The tests use tiny models so running 4-6 tests in parallel on a 24GB gpu works just fine w/o vllm. Using `gpu_memory_utilization` isn't a solution because each test...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: need a GB-based alternative for gpu_memory_utilization feature request;stale ### 🚀 The feature, motivation and pitch I'm struggling to figure out how to extend our test suite to include vllm tests. The problem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cient by doing a rough `gpu_memory_utilization=1/num_workers` because of cuda kernels and other various things and the possibility for the test suite run on different gpus of different sizes, as the tests run on CI with...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: with pytest-xdist - as all tests but on the first worker will fail with OOM. The tests use tiny models so running 4-6 tests in parallel on a 24GB gpu works just fine w/o vllm. Using `gpu_memory_utilization` isn't a solu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
