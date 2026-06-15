# vllm-project/vllm#6328: [Bug]: VLLM's output is unstable version==0.5.1

| 字段 | 值 |
| --- | --- |
| Issue | [#6328](https://github.com/vllm-project/vllm/issues/6328) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM's output is unstable version==0.5.1

### Issue 正文摘录

### Your current environment using version==0.5.1 docker images: command: using model qwen2-GPTQ-Int4 docker run -it --rm --gpus '"device=0,7,8,9"' -p 8090:8090 -e NCCL_P2P_DISABLE=1 -e NCCL_SHM_DISABLE=1 -v /nfs2:/nfs2 -v /var:/var -v /nfs3:/nfs3 -v /nfs5:/nfs5 --shm-size 20g XXXXXXXXX:XXXXXXX python3 -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8090 --model=XXXX/source/deps --served-model-name=qwen2-GPTQ-Int4 --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --seed 42; ### 🐛 Describe the bug I generated 50 results by using http://XXXX/v1/chat/completions with params like: ```markdown "model": "qwen2-GPTQ-Int4", "temperature": 0, "n": 1, "best_of":1, "presence_penalty":0.0, "frequency_penalty":0.0, "repetition_penalty":1.0, "top_p": 1.0, "top_k":1.0, "min_p":0.0 ``` **But I got different results eventhough most of them are the same(>90% are same)**， . Results LIKE: ['P41T33', 'P76T139', 'P76T140', 'P77T142', 'P111T257', 'P111T260', 'P111T261'] ['P41T33', 'P76T139', 'P76T140', 'P77T142', 'P111T257', 'P111T260', 'P111T261'] ['P41T33', 'P76T139', 'P76T140', 'P77T142', 'P111T257', 'P111T260', 'P111T261'] ['P41T33', 'P76T139', 'P77T142', 'P111T257', 'P111T260', 'P11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: VLLM's output is unstable version==0.5.1 bug;stale ### Your current environment using version==0.5.1 docker images: command: using model qwen2-GPTQ-Int4 docker run -it --rm --gpus '"device=0,7,8,9"' -p 8090:8090...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ent using version==0.5.1 docker images: command: using model qwen2-GPTQ-Int4 docker run -it --rm --gpus '"device=0,7,8,9"' -p 8090:8090 -e NCCL_P2P_DISABLE=1 -e NCCL_SHM_DISABLE=1 -v /nfs2:/nfs2 -v /var:/var -v /nfs3:/n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: current environment using version==0.5.1 docker images: command: using model qwen2-GPTQ-Int4 docker run -it --rm --gpus '"device=0,7,8,9"' -p 8090:8090 -e NCCL_P2P_DISABLE=1 -e NCCL_SHM_DISABLE=1 -v /nfs2:/nfs2 -v /var:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e what's causing this. Is it due to the quantized version, or something else? Could you please help check if there's an issue with the parameters? If stability in output is desired, where can I make adjustments?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: VLLM's output is unstable version==0.5.1 bug;stale ### Your current environment using version==0.5.1 docker images: command: using model qwen2-GPTQ-Int4 docker run -it --rm --gpus '"device=0,7,8,9"' -p 8090:8090...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
