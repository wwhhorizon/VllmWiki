# vllm-project/vllm#1172: Can not load Qwen-14B-chat

| 字段 | 值 |
| --- | --- |
| Issue | [#1172](https://github.com/vllm-project/vllm/issues/1172) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can not load Qwen-14B-chat

### Issue 正文摘录

I use the new [Qwen-14B-chat](https://huggingface.co/Qwen/Qwen-14B-Chat/tree/main), and it will raise ``` INFO 09-25 16:20:37 llm_engine.py:72] Initializing an LLM engine with config: model='/data/pretrained_models/Qwen-14B-Chat', tokenizer='/data/pretrained_models/Qwen-14B-Chat', tokenizer_mode=auto, revision=None, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) WARNING 09-25 16:20:37 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. [2023-09-25 16:20:42 +0800] [34243] [ERROR] Exception in worker process Traceback (most recent call last): File "/data/miniconda3/envs/ljh_py311/lib/python3.11/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker worker.init_process() File "/data/miniconda3/envs/ljh_py311/lib/python3.11/site-packages/uvicorn/workers.py", line 66, in init_process super(UvicornWorker, self).init_process() File "/data/miniconda3/envs/ljh_py311/lib/python3.11/site-packages/gunicorn/workers/base.py", line 134, in init_process self.load_wsgi() File "/data/miniconda3/envs/ljh_py311/lib/python3.11/site-package...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Can not load Qwen-14B-chat I use the new [Qwen-14B-chat](https://huggingface.co/Qwen/Qwen-14B-Chat/tree/main), and it will raise ``` INFO 09-25 16:20:37 llm_engine.py:72] Initializing an LLM engine with config: model='/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n-14B-Chat', tokenizer_mode=auto, revision=None, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) WARNING 09-25 16:20:37 tokenizer.py:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: kages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp return util.import_app(self.app_uri) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/miniconda3/envs/ljh_py311/lib/python3.11/site-packages/gunicorn/util.py", line 371,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
