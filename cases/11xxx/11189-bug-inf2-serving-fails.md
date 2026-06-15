# vllm-project/vllm#11189: [Bug]: Inf2 Serving Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#11189](https://github.com/vllm-project/vllm/issues/11189) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inf2 Serving Fails

### Issue 正文摘录

#### Machine - Inf2 EC2 Instance (inf2.8xlarge) - Deep Learning AMI Neuron (Ubuntu 22.04) ``` neuron-ls instance-type: inf2.8xlarge instance-id: i-087c44c67ae0a135f +--------+--------+--------+---------+ | NEURON | NEURON | NEURON | PCI | | DEVICE | CORES | MEMORY | BDF | +--------+--------+--------+---------+ | 0 | 2 | 32 GB | 00:1f.0 | +--------+--------+--------+---------+ ``` #### Code - Cloning repository and building image: ``` git clone https://github.com/vllm-project/vllm.git cd vllm/ docker build -f Dockerfile.neuron -t vllm-neuron . ``` - Running docker container: ``` docker run \ -it \ -p 8000:8000 \ --device /dev/neuron0 \ -e HF_TOKEN=$HF_TOKEN \ -e XLA_IR_DEBUG=1 \ -e XLA_HLO_DEBUG=1 \ vllm-neuron ``` - Serving model: ``` root@7a9735ba8b4d:/app/vllm# vllm serve meta-llama/Llama-3.2-1B --device neuron --tensor-parallel-size 2 --block-size 8 --max-model-len 4096 --max-num-seqs 32 ``` - Logs: ``` INFO 12-14 00:50:03 api_server.py:643] vLLM API server version 0.6.4.post2.dev358+g0d8451c3 INFO 12-14 00:50:03 api_server.py:644] args: Namespace(subparser='serve', model_tag='meta-llama/Llama-3.2-1B', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Inf2 Serving Fails bug;stale #### Machine - Inf2 EC2 Instance (inf2.8xlarge) - Deep Learning AMI Neuron (Ubuntu 22.04) ``` neuron-ls instance-type: inf2.8xlarge instance-id: i-087c44c67ae0a135f +--------+--------...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: f +--------+--------+--------+---------+ | NEURON | NEURON | NEURON | PCI | | DEVICE | CORES | MEMORY | BDF | +--------+--------+--------+---------+ | 0 | 2 | 32 GB | 00:1f.0 | +--------+--------+--------+---------+ ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ``` docker run \ -it \ -p 8000:8000 \ --device /dev/neuron0 \ -e HF_TOKEN=$HF_TOKEN \ -e XLA_IR_DEBUG=1 \ -e XLA_HLO_DEBUG=1 \ vllm-neuron ``` - Serving model: ``` root@7a9735ba8b4d:/app/vllm# vllm serve meta-llama/Llam...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: serve meta-llama/Llama-3.2-1B --device neuron --tensor-parallel-size 2 --block-size 8 --max-model-len 4096 --max-num-seqs 32 ``` - Logs: ``` INFO 12-14 00:50:03 api_server.py:643] vLLM API server version 0.6.4.post2.dev...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='xgrammar', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
