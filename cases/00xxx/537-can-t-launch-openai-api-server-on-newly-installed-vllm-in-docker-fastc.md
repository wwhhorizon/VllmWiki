# vllm-project/vllm#537: Can't launch OpenAI API server on newly installed vLLM in Docker - fastchat not found

| 字段 | 值 |
| --- | --- |
| Issue | [#537](https://github.com/vllm-project/vllm/issues/537) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Can't launch OpenAI API server on newly installed vLLM in Docker - fastchat not found

### Issue 正文摘录

Hi I have a Docker container that I created for vLLM. I built it a few days ago and it worked fine. Today I rebuilt it to get the latest code changes, and now it's failing to launch the OpenAI server. SSHing in to the docker and running the launch command directly shows the following error: ``` vllm@36b7089a5957:~/vllm (main ✔) ᐅ python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/vllm/vllm/vllm/entrypoints/openai/api_server.py", line 17, in from fastchat.model.model_adapter import get_conversation_template ModuleNotFoundError: No module named 'fastchat.model.model_adapter' ``` However I can launch the non-API server fine: ``` vllm@36b7089a5957:~/vllm (main ✔) ᐅ python -m vllm.entrypoints.api_server Downloading (…)lve/main/config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 651/...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Can't launch OpenAI API server on newly installed vLLM in Docker - fastchat not found Hi I have a Docker container that I created for vLLM. I built it a few days ago and it worked fine. Today I rebuilt it to get the lat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: evelopment ci_build;distributed_parallel;frontend_api;model_support cuda;triton build_error;crash;import_error dtype;env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV ca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nizer='facebook/opt-125m', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Downloading (…)okenizer_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lp. development ci_build;distributed_parallel;frontend_api;model_support cuda;triton build_error;crash;import_error dtype;env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 89a5957:~/vllm (main ✔) ᐅ python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | #3 ... #4 [auth] nvidia/cuda:pull token for registry-1.docker.io #4 done 0.0s #3 [internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04 #3 done 0 |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | l rsync less && apt-get clean && rm -rf /var/lib/apt/lists/* #6 cached #7 [ 3/17] run useradd -m -u 1000 vllm && chsh -s /usr/bin/zsh vllm && mkdir -p "/workspace |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | echo "vllm all=(all) nopasswd:all" > /etc/sudoers.d/90-docker-users #7 cached #8 [ 4/17] workdir /home/vllm #8 cached #9 [internal] load build context #9 transferring conte |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
