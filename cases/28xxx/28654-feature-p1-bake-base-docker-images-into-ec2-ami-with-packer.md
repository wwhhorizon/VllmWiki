# vllm-project/vllm#28654: [Feature][P1]: Bake Base Docker Images into EC2 AMI with Packer

| 字段 | 值 |
| --- | --- |
| Issue | [#28654](https://github.com/vllm-project/vllm/issues/28654) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][P1]: Bake Base Docker Images into EC2 AMI with Packer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Currently, every build instance pulls the base Docker images (nvidia/cuda, Python base, PyTorch, etc.) from registries on first use. These base images are large (~8-10GB) and rarely change. By pre-pulling and caching these images in the EC2 AMI using Packer, instances start with a warm cache, eliminating the initial pull time and reducing build times, especially for new/cold instances. ### What You'll Do 1. Analyze which base images are most frequently used: - `nvidia/cuda:12.9.1-devel-ubuntu20.04` - `nvidia/cuda:12.9.1-runtime-ubuntu22.04` - PyTorch images from `download.pytorch.org` - Python base images 2. Modify Packer configuration to: - Pull base images during AMI build - Store them in `/var/lib/docker` - Verify images are properly saved in Docker cache 3. Calculate optimal set of images to bake in (balance AMI size vs. benefit) 4. Set up AMI update automation: - Rebuild AMI monthly or when base images update - Version AMI appropriately - Update Terraform to use new AMI 5. Test that instances launch with pre-cached images 6. Document AMI maintenance procedures ### Deliverables - [ ] Analysis document: which base images t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature][P1]: Bake Base Docker Images into EC2 AMI with Packer feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Currently, every build instance pulls the base Docker images (nvidia...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion Currently, every build instance pulls the base Docker images (nvidia/cuda, Python base, PyTorch, etc.) from registries on first use. These base images are large (~8-10GB) and rarely change. By pre-pulling and cachin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][P1]: Bake Base Docker Images into EC2 AMI with Packer feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Currently, every build instance pulls the base Docker images (nvidia...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ges from `download.pytorch.org` - Python base images 2. Modify Packer configuration to: - Pull base images during AMI build - Store them in `/var/lib/docker` - Verify images are properly saved in Docker cache 3. Calcula...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e - Version AMI appropriately - Update Terraform to use new AMI 5. Test that instances launch with pre-cached images 6. Document AMI maintenance procedures ### Deliverables - [ ] Analysis document: which base images to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
