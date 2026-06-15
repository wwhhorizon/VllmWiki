# vllm-project/vllm#11853: [Bug]: When using PDM, the new Darwin support doesn't work on M1/2/3/4 silicon.

| 字段 | 值 |
| --- | --- |
| Issue | [#11853](https://github.com/vllm-project/vllm/issues/11853) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using PDM, the new Darwin support doesn't work on M1/2/3/4 silicon.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using PDM, the new Darwin support doesn't work on M1/2/3/4 silicon. Inside a completely new pdm project (i.e. directly after pdm init), on MacBook Pro M4 with MacOS 15.2: ``` % pdm add -v git+https://github.com/vllm-project/vllm Adding packages to default dependencies: git+https://github.com/vllm-project/vllm pdm.termui: ======== Start resolving requirements ======== pdm.termui: git+https://github.com/vllm-project/vllm pdm.termui: Adding requirement python==3.11.* pdm.termui: Adding requirement git+https://github.com/vllm-project/vllm unearth.vcs.git: Cloning https://github.com/vllm-project/vllm to /var/folders/2l/j6p8b2gx4pb3227hlrcvfzrw0000gn/T/pdm-build-sxlutwv_ unearth.vcs.git: Resolved https://github.com/vllm-project/vllm to commit 2f7024987e582b85b280909b87287668cd97c92f pdm.termui: Failed to parse pyproject.toml pdm.termui: Running PEP 517 backend to get metadata for pdm.termui: Preparing environment(Isolated mode) for PEP 517 build... pdm.termui: ======== Start resolving requirements ======== pdm.termui: Adding requirement python==3.11.0 pdm.termui: Adding requirement torch==2.5.1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: +https://github.com/vllm-project/vllm Adding packages to default dependencies: git+https://github.com/vllm-project/vllm pdm.termui: ======== Start resolving requirements ======== pdm.termui: git+https://github.com/vllm-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GET_DEVICE automatically set to `cpu` due to macOS pdm.termui: /bin/sh: lsmod: command not found pdm.termui: /bin/sh: lsmod: command not found pdm.termui: running egg_info pdm.termui: creating vllm.egg-info pdm.termui:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: work on M1/2/3/4 silicon. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using PDM, the new Darwin support doesn't work on M1/2/3/4 silicon. Inside a completely ne...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: f pdm.termui: Failed to parse pyproject.toml pdm.termui: Running PEP 517 backend to get metadata for pdm.termui: Preparing environment(Isolated mode) for PEP 517 build... pdm.termui: ======== Start resolving requirement...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ailed to parse pyproject.toml pdm.termui: Running PEP 517 backend to get metadata for pdm.termui: Preparing environment(Isolated mode) for PEP 517 build... pdm.termui: ======== Start resolving requirements ======== pdm....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
