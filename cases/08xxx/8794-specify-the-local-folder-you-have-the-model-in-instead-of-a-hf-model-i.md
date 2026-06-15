# vllm-project/vllm#8794: > > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary files and the model is using a supported architecture, then it will work.

| 字段 | 值 |
| --- | --- |
| Issue | [#8794](https://github.com/vllm-project/vllm/issues/8794) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> > > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary files and the model is using a supported architecture, then it will work.

### Issue 正文摘录

> > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary files and the model is using a supported architecture, then it will work. > > To serve vLLM API: > > ```shell > > #!/bin/bash > > MODEL_NAME="$1" > > test -n "$MODEL_NAME" > > MODEL_DIR="$HOME/models/$MODEL_NAME" > > test -d "$MODEL_DIR" > > python -O -u -m vllm.entrypoints.api_server \ > > --host=127.0.0.1 \ > > --port=8000 \ > > --model=$HOME/models/$MODEL_NAME \ > > --tokenizer=hf-internal-testing/llama-tokenizer > > ``` > > > > > > > > > > > > > > > > > > > > > > > > Serve OpenAI API: > > ```shell > > #!/bin/bash > > MODEL_NAME="$1" > > test -n "$MODEL_NAME" > > MODEL_DIR="$HOME/models/$MODEL_NAME" > > test -d "$MODEL_DIR" > > python -O -u -m vllm.entrypoints.openai.api_server \ > > --host=127.0.0.1 \ > > --port=8000 \ > > --model=$HOME/models/$MODEL_NAME \ > > --tokenizer=hf-internal-testing/llama-tokenizer > > ``` > > > > > > > > > > > > > > > > > > > > > > > > To run on multiple GPUs add: `--tensor-parallel-size=N` where N is the number of GPUs > > The tokenizer above works at least for the Llama 2 based models. It results in faster startup time: `--tokenizer=hf-intern...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: > > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary files and the model is using a supported architecture, then it will work. stale > > Specify the local folder you...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: > > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary files and the model is using a supported architecture, then it will work. stale > > Specify the local folder you...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . If you have all the necessary files and the model is using a supported architecture, then it will work. stale > > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ting/llama-tokenizer` > > Additional parameters you may want to tune: `--block-size` and `--swap-space` > > i used a model meta-llama from huggingface_hub along with vllm eg:- llm = vllm.LLM(model=model_id,gpu_memory_ut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: iles and the model is using a supported architecture, then it will work. stale > > Specify the local folder you have the model in instead of a HF model ID. If you have all the necessary files and the model is using a su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
