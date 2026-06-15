# vllm-project/vllm#9255: [Usage]: running gated models offline

| 字段 | 值 |
| --- | --- |
| Issue | [#9255](https://github.com/vllm-project/vllm/issues/9255) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: running gated models offline

### Issue 正文摘录

### Your current environment I use vllm=0.6.2 installed via pip :-) ### How would you like to use vllm Hello! First of all, thanks for your great service to the community! I appreciate the work you put on this package. I am currently running models with the vLLM server. I am particularly interested in a gated model I have access to, so I followed the [Huggingface Hub instructions](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) for setting a token, downloaded the weights and ran the model successfully. I used: ` vllm serve {model_name} --someotherargs --download-dir /some_local_directory` Until then all good. However, if I want to serve the model without a HF Hub connection (e.g. with no internet or on a fresh session with no HF_TOKEN) I cannot serve it, although the model is downloaded locally: ```python Cannot access gated repo for url https://huggingface.co/ blablabla Access to model {model_id} is restricted. You must have access to it and be authenticated to access it. Please log in. ``` Of course, setting the HF_TOKEN again lets me serve the model (it does not download the weights again). But this is a bit of a bummer as I would...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ated models offline usage ### Your current environment I use vllm=0.6.2 installed via pip :-) ### How would you like to use vllm Hello! First of all, thanks for your great service to the community! I appreciate the work...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: running gated models offline usage ### Your current environment I use vllm=0.6.2 installed via pip :-) ### How would you like to use vllm Hello! First of all, thanks for your great service to the community! I a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
