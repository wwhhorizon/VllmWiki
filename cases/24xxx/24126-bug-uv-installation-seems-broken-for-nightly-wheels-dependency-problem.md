# vllm-project/vllm#24126: [Bug]: uv installation seems broken for nightly wheels (dependency problem with `outlines` and filename<>metadata mismatch)

| 字段 | 值 |
| --- | --- |
| Issue | [#24126](https://github.com/vllm-project/vllm/issues/24126) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: uv installation seems broken for nightly wheels (dependency problem with `outlines` and filename<>metadata mismatch)

### Issue 正文摘录

### Your current environment ```toml # pyproject.toml - a single file in curdir [build-system] requires = ["setuptools>=65", "wheel"] build-backend = "setuptools.build_meta" [project] name = "test_vllm" version = "0.0.0.1" requires-python = ">=3.12" dependencies = [ "vllm", "torch>=2.8", "flash-attn==2.8.2", ] [tool.uv.sources] vllm = { url = "https://vllm-wheels.s3.amazonaws.com/038e9be4eb7a63189c8980845d80cb96957b9919/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl" } ``` ### 🐛 Describe the bug Following: - https://github.com/vllm-project/vllm/pull/20358#issuecomment-3246845686 Installing `pyproject.toml` (`uv sync --active`) leads to a nasty error: ``` × No solution found when resolving dependencies: ╰─▶ Because outlines==0.1.11 depends on outlines-core==0.1.26 and vllm==0.10.1rc2.dev397+g038e9be4e depends on outlines{platform_machine == 's390x'}==0.1.11, we can conclude that vllm==0.10.1rc2.dev397+g038e9be4e and outlines-core{platform_machine != 's390x'}==0.2.10 are incompatible. And because vllm==0.10.1rc2.dev397+g038e9be4e depends on outlines-core{platform_machine != 's390x'}==0.2.10, we can conclude that vllm==0.10.1rc2.dev397+g038e9be4e cannot be used. And because only vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: uv installation seems broken for nightly wheels (dependency problem with `outlines` and filename<>metadata mismatch) bug ### Your current environment ```toml # pyproject.toml - a single file in curdir [build-syst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: htly wheels (dependency problem with `outlines` and filename<>metadata mismatch) bug ### Your current environment ```toml # pyproject.toml - a single file in curdir [build-system] requires = ["setuptools>=65", "wheel"]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e in curdir [build-system] requires = ["setuptools>=65", "wheel"] build-backend = "setuptools.build_meta" [project] name = "test_vllm" version = "0.0.0.1" requires-python = ">=3.12" dependencies = [ "vllm", "torch>=2.8"...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ightly wheels (dependency problem with `outlines` and filename<>metadata mismatch) bug ### Your current environment ```toml # pyproject.toml - a single file in curdir [build-system] requires = ["setuptools>=65", "wheel"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ken for nightly wheels (dependency problem with `outlines` and filename<>metadata mismatch) bug ### Your current environment ```toml # pyproject.toml - a single file in curdir [build-system] requires = ["setuptools>=65"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
