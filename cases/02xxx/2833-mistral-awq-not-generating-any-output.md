# vllm-project/vllm#2833: Mistral AWQ  not generating any output

| 字段 | 值 |
| --- | --- |
| Issue | [#2833](https://github.com/vllm-project/vllm/issues/2833) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mistral AWQ  not generating any output

### Issue 正文摘录

I have tried all the methods mentioned in #2728, but none of them have worked at all,responses are always **empty** I use 2*A6000 for GPU Here is my Docker run command Can anyone help me for this issue?Thank you ! ``` docker run --rm --runtime nvidia --gpus all --env NCCL_P2P_DISABLE=1 --env CUDA_VISIBLE_DEVICES=0,1 --shm-size 10g -p 8002:8002 \ -e MODEL=/app/model \ -e API=se \ -v /home/merge_model/:/app/model \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --ipc=host \ vllm/vllm-openai:latest \ --port 8002 \ --model /app/model/mistral/testtest \ --served-model-name "openchat" \ --max-num-seqs 2000 \ --max-num-batched-tokens 327680 \ --tensor-parallel-size 2 \ --disable-custom-all-reduce \ --enforce-eager \ --quantization 'awq' \ --gpu-memory-utilization 1 \ --max-model-len 21440 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d at all,responses are always **empty** I use 2*A6000 for GPU Here is my Docker run command Can anyone help me for this issue?Thank you ! ``` docker run --rm --runtime nvidia --gpus all --env NCCL_P2P_DISABLE=1 --env CU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LE=1 --env CUDA_VISIBLE_DEVICES=0,1 --shm-size 10g -p 8002:8002 \ -e MODEL=/app/model \ -e API=se \ -v /home/merge_model/:/app/model \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --ipc=host \ vllm/vllm-openai:lat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: l-size 2 \ --disable-custom-all-reduce \ --enforce-eager \ --quantization 'awq' \ --gpu-memory-utilization 1 \ --max-model-len 21440 ``` performance ci_build;distributed_parallel;frontend_api;model_support;quantization...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cker run --rm --runtime nvidia --gpus all --env NCCL_P2P_DISABLE=1 --env CUDA_VISIBLE_DEVICES=0,1 --shm-size 10g -p 8002:8002 \ -e MODEL=/app/model \ -e API=se \ -v /home/merge_model/:/app/model \ -v ~/.cache/huggingfac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: gface:/root/.cache/huggingface \ --ipc=host \ vllm/vllm-openai:latest \ --port 8002 \ --model /app/model/mistral/testtest \ --served-model-name "openchat" \ --max-num-seqs 2000 \ --max-num-batched-tokens 327680 \ --tens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
