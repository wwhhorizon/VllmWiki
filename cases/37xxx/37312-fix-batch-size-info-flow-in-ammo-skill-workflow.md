# vllm-project/vllm#37312: Fix batch size info flow in AMMO skill workflow

| 字段 | 值 |
| --- | --- |
| Issue | [#37312](https://github.com/vllm-project/vllm/issues/37312) |
| 状态 | closed |
| 标签 | nvidia |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Fix batch size info flow in AMMO skill workflow

### Issue 正文摘录

## Summary - **SKILL.md**: Add batch size determination step before `new_target.py`, document `cudagraph_capture_sizes` restriction during nsys profiling, clarify production parity exception - **ammo-researcher.md**: Fix misleading "BS=8 only" to reference all batch sizes from `target.json`, add explicit note about batch size source - **ammo-implementer.md**: Add `target.json` to context gathering checklist, reference batch size source in Gate 5.3 ## Test plan - [ ] Documentation-only changes — no runtime tests needed - [ ] Verify batch size references are consistent across all three files - [ ] Confirm `new_target.py` CLI example matches actual `--batch-sizes` flag 🤖 Generated with [Claude Code](https://claude.com/claude-code)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d**: Add batch size determination step before `new_target.py`, document `cudagraph_capture_sizes` restriction during nsys profiling, clarify production parity exception - **ammo-researcher.md**: Fix misleading "BS=8 onl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: w_target.py`, document `cudagraph_capture_sizes` restriction during nsys profiling, clarify production parity exception - **ammo-researcher.md**: Fix misleading "BS=8 only" to reference all batch sizes from `target.json...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng "BS=8 only" to reference all batch sizes from `target.json`, add explicit note about batch size source - **ammo-implementer.md**: Add `target.json` to context gathering checklist, reference batch size source in Gate...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
