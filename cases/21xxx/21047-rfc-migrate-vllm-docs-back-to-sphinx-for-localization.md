# vllm-project/vllm#21047: [RFC]: Migrate vLLM Docs back to Sphinx for Localization

| 字段 | 值 |
| --- | --- |
| Issue | [#21047](https://github.com/vllm-project/vllm/issues/21047) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Migrate vLLM Docs back to Sphinx for Localization

### Issue 正文摘录

### Motivation. To localize the vLLM Documentation. Recently, I officially published my 1st localization project, `cmake-docs-l10n`, on GitHub: - **Preview:** https://localizethedocs.github.io/cmake-docs-l10n - **Crowdin:** https://localizethedocs.crowdin.com/cmake-docs-l10n - **GitHub:** https://github.com/localizethedocs/cmake-docs-l10n I can confidently say that I can manufacture similar localization projects for any Sphinx-based documentation or website. Originally, I had planned to add `vllm-docs-l10n` to my to-do list, which you can see here: [https://github.com/localizethedocs/projects/issues](https://github.com/localizethedocs/projects/issues) However, I unexpectedly discovered today that the vLLM Documentation has migrated from Sphinx to MkDocs, starting with the [0.9.0](https://github.com/vllm-project/vllm/tree/v0.9.0/docs) tag. - **Commit:** https://github.com/vllm-project/vllm/commit/a1fe24d961d85089c8a254032d35e4bdbca278d6 - **PR:** https://github.com/vllm-project/vllm/pull/18145 This is quite **regrettable** because, based on my research, MkDocs currently doesn't offer the same comprehensive [Internationalization with Gettext](https://www.sphinx-doc.org/en/master/usa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: le ### Motivation. To localize the vLLM Documentation. Recently, I officially published my 1st localization project, `cmake-docs-l10n`, on GitHub: - **Preview:** https://localizethedocs.github.io/cmake-docs-l10n - **Cro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: m sure the vLLM team made this decision after significant discussion and evaluation. However, _if the vLLM Documentation were to migrate back to Sphinx, I would be able to add `vllm-docs-l10n` to my to-do list._ ### Pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /vllm/pull/18145 This is quite **regrettable** because, based on my research, MkDocs currently doesn't offer the same comprehensive [Internationalization with Gettext](https://www.sphinx-doc.org/en/master/usage/advanced...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Migrate vLLM Docs back to Sphinx for Localization RFC;stale ### Motivation. To localize the vLLM Documentation. Recently, I officially published my 1st localization project, `cmake-docs-l10n`, on GitHub: - **Prev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
