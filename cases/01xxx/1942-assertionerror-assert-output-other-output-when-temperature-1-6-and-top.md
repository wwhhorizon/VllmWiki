# vllm-project/vllm#1942: AssertionError assert output == other_output when temperature >= 1.6 and top_p >= 0.9

| 字段 | 值 |
| --- | --- |
| Issue | [#1942](https://github.com/vllm-project/vllm/issues/1942) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError assert output == other_output when temperature >= 1.6 and top_p >= 0.9

### Issue 正文摘录

Hi, I recently attempted to apply two models to run on vllm. At first, everything went smoothly, but after a while, it was discovered that vllm would encounter TP issues that could not be recovered. In the end, I found that this issue is easy to happened in a multi GPU accelerators runtime environment when temperature>=1.6 and top_p >= 0.9. Especially in an environment with 8 GPU accelerators, it basically appears 100%. I tried using the latest 0.2.3 version, but it still appears. The models I tested is as follows: 1、Qwen/Qwen-72B-Chat: https://huggingface.co/Qwen/Qwen-72B-Chat 2、Qwen/Qwen-7B-Chat: https://huggingface.co/Qwen/Qwen-7B-Chat The problem is as follows: File "/usr/local/python-3.8/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 562, in step output = self._run_workers( File "/usr/local/python-3.8/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 718, in _run_workers assert output == other_output

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mperature >= 1.6 and top_p >= 0.9 Hi, I recently attempted to apply two models to run on vllm. At first, everything went smoothly, but after a while, it was discovered that vllm would encounter TP issues that could not...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: erators runtime environment when temperature>=1.6 and top_p >= 0.9. Especially in an environment with 8 GPU accelerators, it basically appears 100%. I tried using the latest 0.2.3 version, but it still appears. The mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ttempted to apply two models to run on vllm. At first, everything went smoothly, but after a while, it was discovered that vllm would encounter TP issues that could not be recovered. In the end, I found that this issue...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ith 8 GPU accelerators, it basically appears 100%. I tried using the latest 0.2.3 version, but it still appears. The models I tested is as follows: 1、Qwen/Qwen-72B-Chat: https://huggingface.co/Qwen/Qwen-72B-Chat 2、Qwen/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
