# vllm-project/vllm#11616: vllm build failure on IBM ppc64le

| 字段 | 值 |
| --- | --- |
| Issue | [#11616](https://github.com/vllm-project/vllm/issues/11616) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm build failure on IBM ppc64le

### Issue 正文摘录

### Your current environment IBM powerpc64le. RHEL 9/ubi9 vllm: Built from source main branch. ### How you are installing vllm ```sh docker build -t vllm:latest -f Dockerfile.ppc64le . ``` Error: ``` 51.54 cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR 51.54 51.54 51.54 Could not find openssl via pkg-config: 51.54 51.54 pkg-config exited with status code 1 51.54 > PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1 pkg-config --libs --cflags openssl 51.54 51.54 The system library `openssl` required by crate `openssl-sys` was not found. 51.54 The file `openssl.pc` needs to be installed and the PKG_CONFIG_PATH environment variable must contain its parent directory. 51.54 The PKG_CONFIG_PATH environment variable is not set. 51.54 51.54 HINT: if you have installed the library, try setting PKG_CONFIG_PATH to the directory containing `openssl.pc`. 51.55 51.55 51.55 cargo:warning=Could not find directory of OpenSSL installation, and this `-sys` crate cannot proceed without this knowledge. If OpenSSL is installed and this crate had trouble finding it, you can set the `OPENSSL_DIR` environment variable for the compilation process. See stderr section below for further information. 51.55 51.55 --- stderr 51...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: vllm build failure on IBM ppc64le installation ### Your current environment IBM powerpc64le. RHEL 9/ubi9 vllm: Built from source main branch. ### How you are installing vllm ```sh docker build -t vllm:latest -f Dockerfi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rfile.ppc64le . ``` Error: ``` 51.54 cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR 51.54 51.54 51.54 Could not find openssl via pkg-config: 51.54 51.54 pkg-config exited with status code 1 51.54 > PKG_CONFIG_ALLOW_S...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -0.6.4-cp310-cp310-linux_ppc64le.whl size=130467 sha256=84914d86dae1fee9efa3cd10af06f5594ee7cfe16fb189af7b0acb7522b26a95 70.55 Stored in directory: /root/.cache/pip/wheels/2a/2e/af/680e384ed0eb6f474586969a6552a57bd8d860...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 6 openssl-sys = 0.9.104 51.56 51.56 51.56 warning: build failed, waiting for other jobs to finish... 63.11 error: `cargo rustc --lib --message-format=json-render-diagnostics --manifest-path Cargo.toml --release -v --fea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
