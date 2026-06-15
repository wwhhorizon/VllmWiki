# vllm-project/vllm#1684: AssertionError assert output == other_output when using source code but works well with 2.1.0 post

| 字段 | 值 |
| --- | --- |
| Issue | [#1684](https://github.com/vllm-project/vllm/issues/1684) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError assert output == other_output when using source code but works well with 2.1.0 post

### Issue 正文摘录

Hello, I'm now using the vllm source code (commit 9f669a9). It works fine when using TP=1 or the number of prompts is small, but when I using 2 GPUs there is the error: ``` File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm-0.2.1-py3.10-linux-x86_64.egg/vllm/entrypoints/llm.py", line 157, in generate return self._run_engine(use_tqdm) File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm-0.2.1-py3.10-linux-x86_64.egg/vllm/entrypoints/llm.py", line 177, in _run_engine step_outputs = self.llm_engine.step() File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm-0.2.1-py3.10-linux-x86_64.egg/vllm/engine/llm_engine.py", line 562, in step output = self._run_workers( File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm-0.2.1-py3.10-linux-x86_64.egg/vllm/engine/llm_engine.py", line 712, in _run_workers assert output == other_output AssertionError ``` And when using the package vllm2.1.0post1 it also works well without any problems. Would you please give advice?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mmit 9f669a9). It works fine when using TP=1 or the number of prompts is small, but when I using 2 GPUs there is the error: ``` File "/opt/conda/envs/vllm/lib/python3.10/site-packages/vllm-0.2.1-py3.10-linux-x86_64.egg/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
