# vllm-project/vllm#4151: [Bug]: Processed prompts:   5%|▌         | 429/8535 [00:27<08:37, 15.68it/s] RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

| 字段 | 值 |
| --- | --- |
| Issue | [#4151](https://github.com/vllm-project/vllm/issues/4151) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Processed prompts:   5%\|▌         \| 429/8535 [00:27<08:37, 15.68it/s] RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

### Issue 正文摘录

### Your current environment 由于是学校服务器 环境无法进行重新设置 目前环境为 vllm==0.2.2+cu118 transformers==4.34.1 python==3.10 ### 🐛 Describe the bug ``` sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm=LLM(model=args.model_dir,trust_remote_code=True) print('model loaded!!!!') good_samples_results= llm.generate(good_samples, sampling_params) ``` 部分代码没有展示出来，bug出现在总共需要推理8000条数据，在推理到第429条时候报错，报错信息如下 ``` File "/home/sft/src/eval_ckpt.py", line 197, in good_samples_results= llm.generate(good_samples, sampling_params) File "/home/.conda/envs/python310/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 157, in generate return self._run_engine(use_tqdm) File "/home/.conda/envs/python310/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 177, in _run_engine step_outputs = self.llm_engine.step() File "/home/.conda/envs/python310/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 562, in step output = self._run_workers( File "/home/.conda/envs/python310/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 700, in _run_workers output = executor(*args, **kwargs) File "/home/.conda/envs/python310/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 1...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: line 719, in forward sample_results = _sample(probs, logprobs, input_metadata) File "/home/.conda/envs/python310/lib/python3.10/site-packages/vllm/model_executor/layers/sampler.py", line 1082, in _sample sample_results...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm=LLM(model=args.model_dir,trust_remote_code=True) print('model loaded!!!!') good_samples_results= llm.generate(good_samples, sampling_params) ``` 部分代码没有展示...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rror: probability tensor contains either `inf`, `nan` or element < 0 bug;stale ### Your current environment 由于是学校服务器 环境无法进行重新设置 目前环境为 vllm==0.2.2+cu118 transformers==4.34.1 python==3.10 ### 🐛 Describe the bug ``` sampli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 码没有展示出来，bug出现在总共需要推理8000条数据，在推理到第429条时候报错，报错信息如下 ``` File "/home/sft/src/eval_ckpt.py", line 197, in good_samples_results= llm.generate(good_samples, sampling_params) File "/home/.conda/envs/python310/lib/python3.10/sit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
