# vllm-project/vllm#28656: [Feature][P1]: Investigate and Implement Zstd Compression for Docker Images

| 字段 | 值 |
| --- | --- |
| Issue | [#28656](https://github.com/vllm-project/vllm/issues/28656) |
| 状态 | open |
| 标签 | feature request;ci/build;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P1]: Investigate and Implement Zstd Compression for Docker Images

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Docker images currently use gzip compression by default. Zstd (Zstandard) is a modern compression algorithm developed by Facebook/Meta that offers better compression ratios and significantly faster decompression speeds compared to gzip. This could reduce image sizes and pull times, especially for the large vLLM images (~30GB). This task investigates whether switching to zstd compression provides measurable benefits. ### What You'll Do 1. **Research Phase** : - Understand Docker's compression options and BuildKit support - Review zstd compression levels (1-19, with 3 as default) - Research ECR compatibility with zstd-compressed layers - Check if containerd/Docker runtime supports zstd decompression 2. **Benchmarking Phase** : - Build vLLM image with default gzip compression - Rebuild with zstd at various compression levels (3, 9, 15) - Measure: image size, build time, push time, pull time, decompression time - Test with both cold cache and warm cache scenarios - Benchmark on actual CI instances (g6.4xlarge) 3. **Implementation Phase** (if justified): - Update Dockerfile and BuildKit configuration - Modify CI pipeline to use zs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature][P1]: Investigate and Implement Zstd Compression for Docker Images feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Docker images currently use gzip compression by default....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1]: Investigate and Implement Zstd Compression for Docker Images feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Docker images currently use gzip compression by default. Zstd (Zsta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: - Check if containerd/Docker runtime supports zstd decompression 2. **Benchmarking Phase** : - Build vLLM image with default gzip compression - Rebuild with zstd at various compression levels (3, 9, 15) - Measure: image...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d compression provides measurable benefits. ### What You'll Do 1. **Research Phase** : - Understand Docker's compression options and BuildKit support - Review zstd compression levels (1-19, with 3 as default) - Research...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: plementation Phase** (if justified): - Update Dockerfile and BuildKit configuration - Modify CI pipeline to use zstd compression - Document compression settings - Deploy to staging and monitor ### Deliverables - [ ] Res...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
