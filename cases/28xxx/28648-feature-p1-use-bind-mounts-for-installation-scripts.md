# vllm-project/vllm#28648: [Feature][P1]:  Use Bind Mounts for Installation Scripts

| 字段 | 值 |
| --- | --- |
| Issue | [#28648](https://github.com/vllm-project/vllm/issues/28648) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P1]:  Use Bind Mounts for Installation Scripts

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Several installation scripts are COPYed into the image, used once, then deleted. This creates unnecessary layers. BuildKit supports bind mounts that make files available during RUN without adding them to the image. ### What You'll Do 1. Identify all script COPY commands: - `install_deepgemm.sh` - `install_gdrcopy.sh` - `install_python_libraries.sh` - `check-wheel-size.py` 2. Replace COPY + RUN + rm pattern with RUN --mount=type=bind 3. Test that scripts execute correctly 4. Document the pattern for future scripts ### Deliverables - [ ] All scripts using bind mounts instead of COPY - [ ] Removed cleanup commands (no longer needed) - [ ] Documentation on bind mount pattern - [ ] Image size comparison ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature][P1]: Use Bind Mounts for Installation Scripts feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Several installation scripts are COPYed into the image, used once, then dele...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][P1]: Use Bind Mounts for Installation Scripts feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Several installation scripts are COPYed into the image, used once, then dele...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: # What You'll Do 1. Identify all script COPY commands: - `install_deepgemm.sh` - `install_gdrcopy.sh` - `install_python_libraries.sh` - `check-wheel-size.py` 2. Replace COPY + RUN + rm pattern with RUN --mount=type=bind...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ize.py` 2. Replace COPY + RUN + rm pattern with RUN --mount=type=bind 3. Test that scripts execute correctly 4. Document the pattern for future scripts ### Deliverables - [ ] All scripts using bind mounts instead of COP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
