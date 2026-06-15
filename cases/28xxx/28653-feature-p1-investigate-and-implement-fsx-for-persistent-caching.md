# vllm-project/vllm#28653: [Feature][P1]: Investigate and Implement FSx for Persistent Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#28653](https://github.com/vllm-project/vllm/issues/28653) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P1]: Investigate and Implement FSx for Persistent Caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Amazon FSx for Lustre is a high-performance shared file system. It's optimized for HPC and build workloads, making it perfect for Docker layer caching. This task investigates using FSx for Lustre as a shared persistent cache across all build instances, with ECR as a fallback. ### What You'll Do 1. Research FSx for Lustre configuration options and best practices 2. Create Terraform configuration for FSx Lustre file system - Determine optimal size (start with 1.2TB minimum) - Choose throughput tier (125 MB/s per TiB is cheapest) - Enable LZ4 compression for space savings - Configure security groups for NFS access 3. Develop mount automation: - Create systemd service to mount FSx on instance boot - Add to Packer AMI configuration - Handle mount failures gracefully (fallback to local) 4. Configure Docker to use FSx-mounted storage 5. Test performance with real builds 6. Compare costs and performance vs ECR-only solution 7. Document setup and troubleshooting procedures ### Deliverables - [ ] Terraform configuration for FSx file system - [ ] Mount automation script (`mount-fsx-cache.sh`) - [ ] Updated Packer AMI with FSx mount - [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 1]: Investigate and Implement FSx for Persistent Caching feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Amazon FSx for Lustre is a high-performance shared file system. It's optimi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ature][P1]: Investigate and Implement FSx for Persistent Caching feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Amazon FSx for Lustre is a high-performance shared file system. It'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ystem - Determine optimal size (start with 1.2TB minimum) - Choose throughput tier (125 MB/s per TiB is cheapest) - Enable LZ4 compression for space savings - Configure security groups for NFS access 3. Develop mount au...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e as a shared persistent cache across all build instances, with ECR as a fallback. ### What You'll Do 1. Research FSx for Lustre configuration options and best practices 2. Create Terraform configuration for FSx Lustre...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nfiguration for FSx storage - [ ] Performance test results (build times, cache hit rates) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
