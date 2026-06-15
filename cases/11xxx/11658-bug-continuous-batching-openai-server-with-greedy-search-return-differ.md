# vllm-project/vllm#11658: [Bug]: Continuous batching (OpenAI Server) with greedy search return different results

| 字段 | 值 |
| --- | --- |
| Issue | [#11658](https://github.com/vllm-project/vllm/issues/11658) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Continuous batching (OpenAI Server) with greedy search return different results

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using greedy decoding (temperature==0.0) for the same gpu and every time we run inference on the same data, the results are a whole lot different To reproduce, first run the api server ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --dtype bfloat16 --enforce-eager --host 0.0.0.0 --port 8011 --gpu-memory-utilization 0.95 ``` Then run (batching with multithread) ``` from openai import OpenAI from tqdm.auto import tqdm from concurrent.futures import ThreadPoolExecutor, as_completed def multithread(func_to_call,list_data,max_workers=8): res = [] with tqdm(total=len(list_data)) as pbar: with ThreadPoolExecutor(max_workers=min(len(list_data),max_workers)) as ex: futures = [ex.submit(func_to_call, k) for k in list_data] for future in as_completed(futures): result = future.result() res.append(result) pbar.update(1) return res def multithread_wrapper(func_to_call,list_data,max_workers=128): from tqdm import trange mthread_inputs = [] for rnd_idx in range(len(list_data)): mthread_inputs.append((rnd_idx,list_data[rnd_idx])) wrapper_func = lambda x:[x[0],func_to_call(x[1])] wrapped_outputs = multithr...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rst run the api server ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --dtype bfloat16 --enforce-eager --host 0.0.0.0 --port 8011 --gpu-memory-utilization 0.95 ``` Then run (batching with multithread) ``` from openai i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Continuous batching (OpenAI Server) with greedy search return different results bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using greedy decoding (temper...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: un inference on the same data, the results are a whole lot different To reproduce, first run the api server ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --dtype bfloat16 --enforce-eager --host 0.0.0.0 --port 8011 --g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ilization 0.95 ``` Then run (batching with multithread) ``` from openai import OpenAI from tqdm.auto import tqdm from concurrent.futures import ThreadPoolExecutor, as_completed def multithread(func_to_call,list_data,max...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: return different results bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using greedy decoding (temperature==0.0) for the same gpu and every time we run inference o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
