# vllm-project/vllm#291: Cannot install neither with pip nor with poetry

| 字段 | 值 |
| --- | --- |
| Issue | [#291](https://github.com/vllm-project/vllm/issues/291) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cannot install neither with pip nor with poetry

### Issue 正文摘录

Got this error with pip (`pip install vllm`): ``` error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> See above for output. note: This error originates from a subprocess, and is likely not a problem with pip. ``` And this error with poetry (`poetry add vllm`): ``` at ~/.local/lib/python3.10/site-packages/poetry/installation/chef.py:152 in _prepare 148│ 149│ error = ChefBuildError("\n\n".join(message_parts)) 150│ 151│ if error is not None: → 152│ raise error from None 153│ 154│ return path 155│ 156│ def _prepare_sdist(self, archive: Path, destination: Path | None = None) -> Path: Note: This error originates from the build backend, and is likely not a problem with poetry but with vllm (0.1.1) not supporting PEP 517 builds. You can verify this by running 'pip wheel --use-pep517 "vllm (==0.1.1)"'. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Cannot install neither with pip nor with poetry installation Got this error with pip (`pip install vllm`): ``` error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Path | None = None) -> Path: Note: This error originates from the build backend, and is likely not a problem with poetry but with vllm (0.1.1) not supporting PEP 517 builds. You can verify this by running 'pip wheel --u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: return path 155│ 156│ def _prepare_sdist(self, archive: Path, destination: Path | None = None) -> Path: Note: This error originates from the build backend, and is likely not a problem with poetry but with vllm (0.1.1) n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
