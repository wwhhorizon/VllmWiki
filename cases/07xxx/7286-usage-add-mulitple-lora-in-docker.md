# vllm-project/vllm#7286: [Usage]: add mulitple lora in docker

| 字段 | 值 |
| --- | --- |
| Issue | [#7286](https://github.com/vllm-project/vllm/issues/7286) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: add mulitple lora in docker

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi I want to attach lora using docker command docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /datadrive/finetune_model/infosys:/app/lora/xyz \ -v /datadrive/finetune_model/dummy:/app/lora/abc \ -p 8000:8000 \ --env "HUGGING_FACE_HUB_TOKEN=" \ vllm/vllm-openai --enable-lora\ --model meta-llama/Meta-Llama-3-8B-Instruct \ --lora-modules xyz-lora=/datadrive/finetune_model/xyz \ --lora-modules abc-lora=/datadrive/finetune_model/abc However, I am getting below error {'object': 'error', 'message': 'The model `xyz-lora` does not exist.', 'type': 'NotFoundError', 'param': None, 'code': 404} Can anyone help here? Did I use wrong command? Thanks you

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: docker command docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /datadrive/finetune_model/infosys:/app/lora/xyz \ -v /datadrive/finetune_model/dummy:/app/lora/abc \ -p 8000:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: add mulitple lora in docker usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi I want to attach lora using docker command docker run --run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
