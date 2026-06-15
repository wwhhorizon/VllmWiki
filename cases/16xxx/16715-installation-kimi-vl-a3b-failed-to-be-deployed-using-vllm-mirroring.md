# vllm-project/vllm#16715: [Installation]: Kimi-VL-A3B failed to be deployed using vllm mirroring

| 字段 | 值 |
| --- | --- |
| Issue | [#16715](https://github.com/vllm-project/vllm/issues/16715) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Kimi-VL-A3B failed to be deployed using vllm mirroring

### Issue 正文摘录

### Your current environment model：Kimi-VL-A3B-Thinking image：vllm-openai：latest vllm version:0.8.4 1.docker pull vllm/vllm-openai 里面的vllm version:0.8.4 2.docker run --gpus all -v /mnt/data1/LargeLanguageModels/qwen:/model --ipc=host --network=host --name kimi-vl -it --entrypoint vllm/vllm-openai ：latest bash 3. 在容器中如下命令启动大模型 > CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \ --port 3000 \ --served-model-name kimi-vl \ --trust-remote-code \ --model /models/Kimi-VL-A3B-Thinking/Kimi-VL-A3B-Thinking \ --tensor-parallel-size 1 \ --max-num-batched-tokens 131072 \ --max-model-len 131072 \ --max-num-seqs 512 \ --limit-mm-per-prompt image=256 \ --disable-mm-preprocessor-cache 出现报错 > Traceback (most recent call last): File "/usr/local/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/local/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/gwm-tmp/kimi_vl/vllm/vllm/entrypoints/openai/api_server.py", line 1121, in uvloop.run(run_server(args)) File "/gwm-tmp/kimi_vl/venv/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) Fil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Kimi-VL-A3B failed to be deployed using vllm mirroring installation ### Your current environment model：Kimi-VL-A3B-Thinking image：vllm-openai：latest vllm version:0.8.4 1.docker pull vllm/vllm-openai
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: deployed using vllm mirroring installation ### Your current environment model：Kimi-VL-A3B-Thinking image：vllm-openai：latest vllm version:0.8.4 1.docker pull vllm/vllm-openai 里面的vllm version:0.8.4 2.docker run --gpus all...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: i-vl -it --entrypoint vllm/vllm-openai ：latest bash 3. 在容器中如下命令启动大模型 > CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \ --port 3000 \ --served-model-name kimi-vl \ --trust-remote-code \ --model /mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Your current environment model：Kimi-VL-A3B-Thinking image：vllm-openai：latest vllm version:0.8.4 1.docker pull vllm/vllm-openai 里面的vllm version:0.8.4 2.docker run --gpus all -v /mnt/data1/LargeLanguageModels/qwen:/model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
