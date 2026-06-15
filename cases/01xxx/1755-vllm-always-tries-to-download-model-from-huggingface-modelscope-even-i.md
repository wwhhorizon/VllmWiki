# vllm-project/vllm#1755: vllm always tries to download model from huggingface/modelscope even if I specify --download-dir  with already downloaded models

| 字段 | 值 |
| --- | --- |
| Issue | [#1755](https://github.com/vllm-project/vllm/issues/1755) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm always tries to download model from huggingface/modelscope even if I specify --download-dir  with already downloaded models

### Issue 正文摘录

The situation: I've downloaded the huge models on my server. And hope vllm could load the model. the structure of the model dir: ``` $ ls /data/vllm.model/01ai/Yi-34B-200K/ ``` ``` LICENSE generation_config.json pytorch_model-00004-of-00007.bin tokenizer.json README.md md5 pytorch_model-00005-of-00007.bin tokenizer.model Yi.svg modeling_yi.py pytorch_model-00006-of-00007.bin tokenizer_config.json config.json pytorch_model-00001-of-00007.bin pytorch_model-00007-of-00007.bin configuration.json pytorch_model-00002-of-00007.bin pytorch_model.bin.index.json configuration_yi.py pytorch_model-00003-of-00007.bin tokenization_yi.py ``` Try to load the mode as: ``` VLLM_USE_MODELSCOPE=True python -m vllm.entrypoints.openai.api_server --model 01ai/Yi-34B-200K --download-dir /data/vllm.model/ --host 0.0.0.0 --trust-remote-code ``` But it always tries to download the huge model files: ``` $VLLM_USE_MODELSCOPE=True python -m vllm.entrypoints.openai.api_server --model 01ai/Yi-34B-200K --download-dir /data/vllm.model/ --host 0.0.0.0 --trust-remote-code ``` ``` INFO 11-22 22:04:27 api_server.py:638] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vllm always tries to download model from huggingface/modelscope even if I specify --download-dir with already downloaded models The situation: I've downloaded the huge models on my server. And hope vllm could load the m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: always tries to download model from huggingface/modelscope even if I specify --download-dir with already downloaded models The situation: I've downloaded the huge models on my server. And hope vllm could load the model....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _remote_code=True, download_dir='/data/vllm.model/', load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, block_size=16, seed=0, swap_space=4, gpu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:638] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='01ai/Yi-34B-200K', tokenizer=None, revisi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: le_log_stats=False, quantization=None, engine_use_ray=False, disable_log_requests=False, max_log_len=None) 2023-11-22 22:04:27,237 - modelscope - INFO - PyTorch version 2.1.0 Found. 2023-11-22 22:04:27,238 - modelscope...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
