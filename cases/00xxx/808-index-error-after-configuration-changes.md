# vllm-project/vllm#808: Index error after configuration changes

| 字段 | 值 |
| --- | --- |
| Issue | [#808](https://github.com/vllm-project/vllm/issues/808) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Index error after configuration changes

### Issue 正文摘录

Hi there, Previously I run into an exception showing that there is no enough swap space, as in #787 . I modify the parameter `swap_space` in `EngineArgs` from 4 to 32 accordingly, and the number of CPU blocks raise proportionally. However, I encounter another `IndexError` exception: ``` Traceback (most recent call last): File "yyy.py", line 65, in main outputs = llm.generate(prompts, sampling_params) File "/xxx/.local/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 130, in generate return self._run_engine(use_tqdm) File "/xxx/.local/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 150, in _run_engine step_outputs = self.llm_engine.step() File "/xxx/.local/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 313, in step output = self._run_workers( File "/xxx/.local/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 470, in _run_workers output = executor(*args, **kwargs) File "/xxx/.local/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/xxx/.local/lib/python3.9/site-packages/vllm/worker/worker.py", line 289, in execute_model input_tokens, input_positions, input_metadata...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: p_space` in `EngineArgs` from 4 to 32 accordingly, and the number of CPU blocks raise proportionally. However, I encounter another `IndexError` exception: ``` Traceback (most recent call last): File "yyy.py", line 65, i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Index error after configuration changes Hi there, Previously I run into an exception showing that there is no enough swap space, as in #787 . I modify the parameter `swap_space` in `EngineArgs` from 4 to 32 accordingly,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
