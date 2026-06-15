# vllm-project/vllm#1967: Streaming broken in OpenAI server in v0.2.3 (0.2.2 works)

| 字段 | 值 |
| --- | --- |
| Issue | [#1967](https://github.com/vllm-project/vllm/issues/1967) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Streaming broken in OpenAI server in v0.2.3 (0.2.2 works)

### Issue 正文摘录

After upgrading to the new 0.2.3, I get the following error on a Mistral 7B finetune. I am not really sure what the cause is of the `output.logprobs` being `None`. I suspect the error is being thrown after one of these PRs: #1504 #1756 (probably first one) Python Code: ```python from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", ) models = client.models.list() model = models.data[0].id completion = client.completions.create( model=model, prompt="Testing sequence", stream=True, temperature=0.8, max_tokens=512 ) for c in completion: print(c.choices[0].text, end="") ``` Traceback: ```bash INFO 12-07 17:44:59 api_server.py:711] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', model='/mnt/workspace/', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='safetensors', dtype='float16', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: , trust_remote_code=False, download_dir=None, load_format='safetensors', dtype='float16', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, bl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", ) models = client.models.list() model = models.data[0].id completion = client.completions.create( model=model, prompt="Testing sequence", stream=True, temper...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: anaconda/envs/azureml_py310_sdkv2/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/anaconda/envs/azureml_py310_sdkv2/lib/python3.10/site-packages/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s: #1504 #1756 (probably first one) Python Code: ```python from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", ) models = client.models.list() model = models.data[0].id compl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:711] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
