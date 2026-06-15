# vllm-project/vllm#2558: Issue while loading the model finetuned trained from h2o llm studio

| 字段 | 值 |
| --- | --- |
| Issue | [#2558](https://github.com/vllm-project/vllm/issues/2558) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue while loading the model finetuned trained from h2o llm studio

### Issue 正文摘录

Using below command `docker run -p 8080:8080 --gpus=all -e MODEL=/home/workspace/output/user/Experiment_Name/unzip_model/ api ` Content of unzip_model : This folder contains the unzip of model finetuned using h2o llm studio ``` config.json model_card.md pytorch_model.bin.index.json pytorch_model-00001-of-00002.bin pytorch_model-00002-of-00002.bin special_tokens_map.json tokenizer.json generation_config.json tokenizer_config.json ``` Traceback ``` Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/transformers/utils/hub.py", line 389, in cached_file resolved_file = hf_hub_download( File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_validators.py", line 110, in _inner_fn validate_repo_id(arg_value) File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_validators.py", line 158, in validate_repo_id raise HFValidationError( huggingface_hub.utils._validators.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/home/workspace/output/user/Experiment_Name/unzip_model/'. Use `repo_type` argument if needed. The above exception was the direct cause of the following exception: Traceback (most recen...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Issue while loading the model finetuned trained from h2o llm studio Using below command `docker run -p 8080:8080 --gpus=all -e MODEL=/home/workspace/output/user/Experiment_Name/unzip_model/ api ` Content of unzip_model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ing the model finetuned trained from h2o llm studio Using below command `docker run -p 8080:8080 --gpus=all -e MODEL=/home/workspace/output/user/Experiment_Name/unzip_model/ api ` Content of unzip_model : This folder co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
