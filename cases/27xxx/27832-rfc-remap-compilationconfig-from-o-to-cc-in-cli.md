# vllm-project/vllm#27832: [RFC]: Remap `CompilationConfig` from `-O` to `-cc` in CLI

| 字段 | 值 |
| --- | --- |
| Issue | [#27832](https://github.com/vllm-project/vllm/issues/27832) |
| 状态 | closed |
| 标签 | help wanted;good first issue;RFC;torch.compile |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Remap `CompilationConfig` from `-O` to `-cc` in CLI

### Issue 正文摘录

### Motivation. With #20283 (and #26847), we're repurposing `-O0`/`-O1`/`-O2`/`-O3` to map to `optimization_level` instead of `CompilationConfig.level`/`CompilationConfig.mode`. This leaves us in a slightly confusing state where `-O` can refer to optimization level or compilation config depending on what follows it: - `-O0` -> `optimization_level=0` - `-O 3` -> `optimization_level=3` - `-O {"cudagraph_mode": "NONE"}` -> `CompilationConfig(cudagraph_mode="NONE")` - `-O.use_inductor=False` -> `CompilationConfig(use_inductor=False)` - `--compilation-config.backend=eager` -> `CompilationConfig(backend="eager")` This is bad UX, and we should fix it. However, a CLI shorthand for `CompilationConfig` is still needed so users can easily compose different properties. ### Proposed Change. We should create a new shorthand for `CompilationConfig` should be `-cc`. Other options are `-c` and `-C`, but as discussed [here](https://github.com/vllm-project/vllm/pull/26847#discussion_r2439248068), single letters are not "pythonic" and capital letters are worse (extra `Shift` keystroke + less pythonic). However, the exact shorthand is up for discussion. React below to cast your vote. Example changes:...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: O0` -> `optimization_level=0` - `-O 3` -> `optimization_level=3` - `-O {"cudagraph_mode": "NONE"}` -> `CompilationConfig(cudagraph_mode="NONE")` - `-O.use_inductor=False` -> `CompilationConfig(use_inductor=False)` - `--...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: alse` -> `CompilationConfig(use_inductor=False)` - `--compilation-config.backend=eager` -> `CompilationConfig(backend="eager")` This is bad UX, and we should fix it. However, a CLI shorthand for `CompilationConfig` is s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Config` from `-O` to `-cc` in CLI help wanted;good first issue;RFC;torch.compile ### Motivation. With #20283 (and #26847), we're repurposing `-O0`/`-O1`/`-O2`/`-O3` to map to `optimization_level` instead of `Compilation...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: NE"}` -> `CompilationConfig(cudagraph_mode="NONE")` - `-O.use_inductor=False` -> `CompilationConfig(use_inductor=False)` - `--compilation-config.backend=eager` -> `CompilationConfig(backend="eager")` This is bad UX, and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC]: Remap `CompilationConfig` from `-O` to `-cc` in CLI help wanted;good first issue;RFC;torch.compile ### Motivation. With #20283 (and #26847), we're repurposing `-O0`/`-O1`/`-O2`/`-O3` to map to `optimization_level...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
