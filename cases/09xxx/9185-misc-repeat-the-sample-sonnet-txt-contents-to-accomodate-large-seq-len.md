# vllm-project/vllm#9185: [Misc]: Repeat the sample sonnet.txt contents to accomodate large seq lengths in benchmarking

| 字段 | 值 |
| --- | --- |
| Issue | [#9185](https://github.com/vllm-project/vllm/issues/9185) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Repeat the sample sonnet.txt contents to accomodate large seq lengths in benchmarking

### Issue 正文摘录

### Anything you want to discuss about vllm. While running [serving benchmarks](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py) with following command. `python benchmark_serving.py --backend vllm --model meta-llama/Llama-3.1-405B-Instruct --dataset-name sonnet --num-prompt=1 --dataset-path="sonnet.txt" --sonnet-input-len 32000` The following error is issued: ``` WARNING 10-09 06:56:51 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. /opt/conda/envs/py_3.10/lib/python3.10/site-packages/torchvision-0.16.1+fdea156-py3.10-linux-x86_64.egg/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: '/opt/conda/envs/py_3.10/lib/python3.10/site-packages/torchvision-0.16.1+fdea156-py3.10-linux-x86_64.egg/torchvision/image.so: undefined symbol: _ZN3c1017RegisterOperatorsD1Ev'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source? warn( Namespace(backend='vllm', base_url=None, host=...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Repeat the sample sonnet.txt contents to accomodate large seq lengths in benchmarking ### Anything you want to discuss about vllm. While running [serving benchmarks](https://github.com/vllm-project/vllm/blob/main/benchm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: torchvision-0.16.1+fdea156-py3.10-linux-x86_64.egg/torchvision/image.so: undefined symbol: _ZN3c1017RegisterOperatorsD1Ev'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: y) with following command. `python benchmark_serving.py --backend vllm --model meta-llama/Llama-3.1-405B-Instruct --dataset-name sonnet --num-prompt=1 --dataset-path="sonnet.txt" --sonnet-input-len 32000` The following...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -len 32000` The following error is issued: ``` WARNING 10-09 06:56:51 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. /opt/conda/envs/py_3.10/lib/python...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: a/Llama-3.1-405B-Instruct', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1, logprobs=None, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=False, metada...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
