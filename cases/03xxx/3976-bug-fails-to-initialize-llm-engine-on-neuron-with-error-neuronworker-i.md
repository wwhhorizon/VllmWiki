# vllm-project/vllm#3976: [Bug]: Fails to initialize LLM engine on neuron with error - NeuronWorker.__init__() missing 1 required positional argument: 'cache_config'

| 字段 | 值 |
| --- | --- |
| Issue | [#3976](https://github.com/vllm-project/vllm/issues/3976) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fails to initialize LLM engine on neuron with error - NeuronWorker.__init__() missing 1 required positional argument: 'cache_config'

### Issue 正文摘录

### Environment ```text (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ python --version Python 3.10.12 (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ pip list | grep torch torch 2.1.2 torch-neuronx 2.1.2.2.1.0 torch-xla 2.1.2 torchvision 0.16.2 (aws_neuronx_venv_transformers_neuronx) uubuntu@ip-172:~/vllm$ vi requirements-neuron.txt (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ pip list | grep vllm vllm 0.4.0.post1+neuron213 (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ ``` ### Code to reproduce ```code from vllm import LLM, SamplingParams sampling_params = SamplingParams(n=1, temperature=0.0, max_tokens=2048) model_id='mistralai/Mixtral-8x7B-v0.1' llm = LLM( model=model_id, max_num_seqs=8, # The max_model_len and block_size arguments are required to be same as # max sequence length when targeting neuron device. # Currently, this is a known limitation in continuous batching support # in transformers-neuronx. # TODO(liangfu): Support paged-attention in transformers-neuronx. max_model_len=128, block_size=128, # The device can be automatically detected when AWS Neuron SDK is installed. # The device argument can be either u...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ python --version Python 3.10.12 (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ pip list | grep torch torch 2.1.2 torch-neuronx 2.1.2.2.1.0 t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: er.__init__() missing 1 required positional argument: 'cache_config' bug;stale ### Environment ```text (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ python --version Python 3.10.12 (aws_neuronx_venv_tran...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, enforce_eager, max_context_len_to_capture, disable_cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: - NeuronWorker.__init__() missing 1 required positional argument: 'cache_config' bug;stale ### Environment ```text (aws_neuronx_venv_transformers_neuronx) ubuntu@ip-172:~/vllm$ python --version Python 3.10.12 (aws_neuro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ig 33 ), "Speculative decoding not yet supported for Neuron backend." 35 # Instantiate the worker and load the model to the device. ---> 36 self._init_worker() File /opt/aws_neuronx_venv_transformers_neuronx/lib/python3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
